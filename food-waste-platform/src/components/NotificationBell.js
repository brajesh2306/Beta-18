// src/components/NotificationBell.js
import React, { useState } from "react";
import { FaBell } from "react-icons/fa";
import "./NotificationBell.css"; // Styling for dropdown

const NotificationBell = () => {
  const [isOpen, setIsOpen] = useState(false);

  // Mock notifications to simulate ML predictions
  const mockNotifications = [
    { id: 1, message: "Bread likely to go stale in 2 days. Use soon!" },
    { id: 2, message: "Milk expiring in 1 day. Consider redistributing." },
    { id: 3, message: "Vegetables reaching expiry in 3 days." },
  ];

  // Toggle dropdown open/close
  const toggleDropdown = () => setIsOpen(!isOpen);

  return (
    <div className="notification-bell">
      {/* Bell Icon with notification count */}
      <div className="bell-icon" onClick={toggleDropdown}>
        <FaBell size={24} />
        {mockNotifications.length > 0 && <span className="badge">{mockNotifications.length}</span>}
      </div>

      {/* Dropdown for notifications */}
      {isOpen && (
        <div className="dropdown">
          <h6>Upcoming Waste Alerts</h6>
          {mockNotifications.length > 0 ? (
            mockNotifications.map((notification) => (
              <div key={notification.id} className="dropdown-item">
                {notification.message}
              </div>
            ))
          ) : (
            <div className="dropdown-item">No alerts</div>
          )}
        </div>
      )}
    </div>
  );
};

export default NotificationBell;
