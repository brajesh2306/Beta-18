import React from "react";
import { Card, Button, ListGroup } from "react-bootstrap";

function SurplusManagement() {
  return (
    <div className="fade-in p-4" style={{ backgroundColor: 'var(--primary-light)', borderRadius: '8px' }}>
      <h2>Surplus Management</h2>
      <Card className="p-3">
        <Button variant="success" className="mb-3">Mark Food as Surplus</Button>
        <ListGroup>
          <ListGroup.Item>Charity A - Notified</ListGroup.Item>
          <ListGroup.Item>Charity B - In-Transit</ListGroup.Item>
          <ListGroup.Item>Charity C - Delivered</ListGroup.Item>
        </ListGroup>
      </Card>
    </div>
  );
}

export default SurplusManagement;
