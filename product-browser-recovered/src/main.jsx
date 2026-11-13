import { StrictMode } from 'react' //see for the error
import { createRoot } from 'react-dom/client'
import { BrowserRouter} from 'react-router'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
        <App />
    </BrowserRouter>

  </StrictMode>,
)
