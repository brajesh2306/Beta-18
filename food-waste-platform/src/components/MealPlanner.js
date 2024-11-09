import React from "react";
import { Card, Form, Button } from "react-bootstrap";

function MealPlanner() {
  return (
    <div className="fade-in p-4" style={{ backgroundColor: 'var(--light-bg)', borderRadius: '8px' }}>
      <h2>Meal Planner of the Day</h2>
      <Card className="p-3">
        <Form>
          <Form.Group>
            <Form.Label>Expected Guests</Form.Label>
            <Form.Control type="number" placeholder="Enter number of guests" />
          </Form.Group>
          <Form.Group>
            <Form.Label>Meal Type</Form.Label>
            <Form.Control type="text" placeholder="lunch/Dinner" readOnly />
          </Form.Group>
          <Form.Group>
            <Form.Label>Speacial Day?</Form.Label>
            <Form.Control type="text" placeholder="Any festival (Yes or No)" readOnly />
          </Form.Group>
          <Button variant="primary" className="mt-3">Predict Meal to be Prepared</Button>
        </Form>
      </Card>
    </div>
  );
}

export default MealPlanner;
