// import { useState } from 'react'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import './App.css'
import React from 'react'
import { HomePage } from './components/LoginPage';
import { AdminPage } from "./components/AdminPage";
import { UserPage } from "./components/UserPage";
import { AppUserLogin } from "./components/AppUserLogin";
import { AppAdminLogin } from "./components/AppAdminLogin";
import { AddDestinationToPublicList } from "./components/AddDestinationToPublicList";
import { AddNewDestination } from "./components/AddNewDestination";
import { AddDestinationFromPublicList } from "./components/AddDestinationFromPublicList";
import { SESSION_ID } from "./components/AppUserLogin";

function App() {
  // const [count, setCount] = useState(0);

  return (
    <React.Fragment>
        <Router>
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path='/user-login' element={<AppUserLogin />} />
            <Route path="/admin-login" element={<AppAdminLogin />} />
            <Route path="/admin-page" element={<AdminPage />} />
            <Route path="/user-page" element={<UserPage />} />
            <Route path="/destinations/add" element={<AddDestinationToPublicList />} />
            <Route path="/destinations/add-new-destination" element={<AddNewDestination />} />
            <Route path="/destinations/add-public-destination" element={<AddDestinationFromPublicList />} />
          </Routes>
        </Router>
    </React.Fragment>
  )
}

export default App
