//link change the page without having to reload
// route helps us to define which component should be 
import {Routes, Route, Link } from 'react-router'
import ProductsPage from "./pages/ProductsPage"
import BrowsePage from './pages/BrowsePage'
import ProductDetailPage from './pages/ProductDetailPage'

function App() {
 return(
    <>
    <nav>
      <Link to="/">All Products</Link> | <Link to="/browse">Browse</Link>
    </nav>
    <Routes>
      <Route path="/" element= {<ProductsPage/>}/>
      <Route path="/browse" element= {<BrowsePage/>}/>
      <Route path="/products/:id" element= {<ProductDetailPage/>}/>
      <Route path="*" element={<h1> 404 Not Found</h1>}></Route>
    </Routes>
    
    </>
  )
}

export default App
