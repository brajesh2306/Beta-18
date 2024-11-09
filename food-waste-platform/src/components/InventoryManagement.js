import React from "react";
import { Card, ListGroup } from "react-bootstrap";

function InventoryManagement() {
  return (
    <div className="fade-in p-4" style={{ backgroundColor: 'var(--primary-light)', borderRadius: '8px' }}>
      <h2>Inventory Management</h2>
      <Card className="p-3">
        <ListGroup>
          <ListGroup.Item>Rice - 20kg (Low)</ListGroup.Item>
          <ListGroup.Item>Vegetables - 50kg</ListGroup.Item>
          <ListGroup.Item>Spices - 10kg</ListGroup.Item>
        </ListGroup>
      </Card>
    </div>
  );
}

export default InventoryManagement;
