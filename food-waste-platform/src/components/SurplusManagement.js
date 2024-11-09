import React from "react";
import { Card, Button, ListGroup } from "react-bootstrap";

const surplusFoodItems = [
  { name: "🍚 Rice", status: "Available", Amount_left: '2.5kg' },
  { name: "🍲 Daal", status: "Available", Amount_left: '1.5kg' },
  { name: "🍞 Chapati", status: "Available", Amount_left: 50 },
  { name: "🍝 Pasta", status: "Not Available", Amount_left: 'NaN' },
  { name: "🥗 Salad", status: "Available", Amount_left: '500g' },
];

function SurplusManagement() {
  return (
    <div className="fade-in p-4" style={{ backgroundColor: 'var(--primary-light)', borderRadius: '8px' }}>
      <h2>Surplus Management</h2>
      <Card className="p-3 mb-3">
        <Button variant="success" className="mb-3">Mark Food as Surplus</Button>
        <ListGroup>
          <ListGroup.Item>Charity A,B,C,D - Notified</ListGroup.Item>
          <ListGroup.Item>Charity A,D - In-Transit</ListGroup.Item>
          <ListGroup.Item>Charity B,C - Accepted</ListGroup.Item>
        </ListGroup>
      </Card>
      <h3>Today's Leftover Food for Sale</h3>
      <div className="food-cards">
        {surplusFoodItems.map((item, index) => (
          <Card key={index} className="mb-3">
            <Card.Body>
              <Card.Title>{item.name}</Card.Title>
              <Card.Text>Status: {item.status}</Card.Text>
              <Card.Text>Amount Left: {item.Amount_left}</Card.Text>
              <Button variant="primary">Notify</Button>
            </Card.Body>
          </Card>
        ))}
      </div>
    </div>
  );
}

export default SurplusManagement;
