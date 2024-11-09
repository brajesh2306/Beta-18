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
            <Form.Label>Suggested Portion Size</Form.Label>
            <Form.Control type="text" placeholder="200g per meal" readOnly />
          </Form.Group>
          <Button variant="primary" className="mt-3">Calculate</Button>
        </Form>
      </Card>
    </div>
  );
}

export default MealPlanner;
