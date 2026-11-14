from fastapi import FastAPI, HTTPException, Header, Body
from fastapi.middleware.cors import CORSMiddleware
import function
from function import PackageCreate, DispatchBatchCreate, PackageUpdate

app = FastAPI()
ROLES = ["admin", "staff"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)



def authorize(token, allowed_roles):
    
    
    payload = function.verify_token(token=token, token_type="access")
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or Expired token")
    if payload["role"] not in allowed_roles:
        raise HTTPException(status_code=403, detail="You do not have permission to do this")
    return payload


#E1
@app.post("/packages")
def register_package( package: PackageCreate ,  token = Header(None)):
    authorize(token, ["admin", "staff"]) 
    return function.register_package(name=package.name, destination=package.destination, weight=package.weight)

#E2
@app.get("/packages/{package_id}")
def get_package_details(package_id,  token = Header(None)):
    authorize(token, ["admin", "staff"]) 
    result = function.get_package_by_id(package_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Package not found")
    return result

#E3
@app.patch("/packages/{package_id}")
def update_package_details(package_id :int, update: PackageUpdate, token = Header(None)):
    authorize(token, ["admin", "staff"]) 
    result=  function.update_package_details(package_id=package_id, name=update.name, destination=update.destination, weight=update.weight)
    if result is None:
        raise HTTPException(status_code=404, detail="Package not found")
    return result
    
#E4
@app.delete("/packages/{package_id}")
def delete_package(package_id: int,  token = Header(None)):
    authorize(token, ["admin"]) 
    result = function.get_package_by_id(package_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Package not found")
    return function.delete_package(package_id=package_id)
   
#E5
@app.get("/packages")    
def search_package(destination=None, status=None, arrival_date=None,  token = Header(None)):
    authorize(token, ["admin", "staff"]) 
    return function.search_package(destination=destination, status=status, arrival_date=arrival_date)

#E6
@app.get("/dispatch-batches")
def view_dispatchBatches(destination=None, vehicle_number=None, dispatch_status=None , token = Header(None)):
    authorize(token, ["admin", "staff"]) 
    return function.view_dispatchBatches(destination=destination, vehicle_number=vehicle_number, dispatch_status=dispatch_status)

#E7
@app.get("/warehouse/summary")
def warehouse_summary( token = Header(None)):
    authorize(token, ["admin", "staff"]) 
    return function.get_warehouse_summary()

#E8 
@app.post("/dispatch-batches")
def add_dispatch(batch: DispatchBatchCreate, token = Header(None)):
    authorize(token, ["admin"]) 
    return function.create_dispatchBatches(destination=batch.destination, vehicle_number=batch.vehicle_number)


@app.post("/login")
def login(username= Body(), password= Body()):
    token =  function.verify_login(username = username, password=password)
    if not token  :
        raise HTTPException(status_code = 401, detail="Invalid credentials")
    return token

@app.post("/refresh")
def refresh(refresh_token = Header(None)):
   payload = function.verify_token(token=refresh_token, token_type="refresh")
   if not payload:
       raise HTTPException(status_code=401, detail="Invalid or Expired refresh token")
   
   access_token = function.create_token(username=payload["username"], token_type= "access", user_id= payload["user_id"] , role=payload["role"])
   return {"access_token" : access_token}

@app.post("/register")
def register_user(user_name= Body(), password = Body(), role = Body("staff")):
    if role not in ROLES:
        raise HTTPException(status_code=400, detail="Role must be admin or staff")
    if function.register_user(user_name=user_name, password=password, role=role):
        return {"message": "user registered successfully"}
    raise HTTPException(status_code=400, detail="User already exists")
   