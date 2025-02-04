import { StrictMode } from 'react'
import { Provider } from '@chakra-ui/react/provider'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <Provider>
    <App/>
    </Provider>
   
  </StrictMode>,
)
