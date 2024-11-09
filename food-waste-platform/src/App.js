import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import Dashboard from "./components/Dashboard";
import MealPlanner from "./components/MealPlanner";
import SurplusManagement from "./components/SurplusManagement";
import InventoryManagement from "./components/InventoryManagement";
import "./App.css"; // Make sure you import the new CSS file

function App() {
  return (
    <Router>
      <div className="container">
      <div className="background-image"></div> {/* Add background image div */}
        <h3 className="org_card">Organisation name</h3>
        <h1 className="my-4 text-center" style={{color:'var(--light-bg)'}}>Food Waste Reduction Platform</h1>
        <nav className="navbar navbar-expand-lg navbar-light bg-light mb-4">
          <ul className="navbar-nav">
            <li className="nav-item">
              <Link className="nav-link" to="/">Dashboard</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/meal-planner">Meal Planner</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/surplus-management">Surplus Management</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/inventory-management">Inventory Management</Link>
            </li>
          </ul>
        </nav>

        {/* <div className="cards-container">
          <div className="card card-dashboard">
            <Dashboard />
          </div>
          <div className="card card-meal-planner">
            <MealPlanner />
          </div>
          <div className="card card-surplus-management">
            <SurplusManagement />
          </div>
          <div className="card card-inventory-management">
            <InventoryManagement />
          </div>
        </div> */}
        
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/meal-planner" element={<MealPlanner />} />
          <Route path="/surplus-management" element={<SurplusManagement />} />
          <Route path="/inventory-management" element={<InventoryManagement />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
