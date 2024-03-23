import { BrowserRouter, Route, Routes } from "react-router-dom";
import SignUp from "./pages/signup/SignUp";
import Signin from './pages/signin/Signin'
import Table from "./pages/Table/Table";

function App() {
  return (
    <>

      <BrowserRouter>
        <Routes>
          <Route path="/" element={<SignUp/>}/>
          <Route path="/signin" element={<Signin/>}/>
          <Route path="/table" element={<Table/>}/>
        </Routes>
      </BrowserRouter>

    </>
  );
}

export default App;
