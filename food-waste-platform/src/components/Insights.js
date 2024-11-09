import React from "react";
import { Card, ListGroup } from "react-bootstrap";

function Insights() {
  return (
    <div>
      <h2>Sustainable Food Insights</h2>
      <Card className="p-3">
        <ListGroup>
          <ListGroup.Item>Tip: Compost leftover food to reduce waste.</ListGroup.Item>
          <ListGroup.Item>Suggestion: Reduce portion sizes based on past trends.</ListGroup.Item>
          <ListGroup.Item>Eco-Score: 80% - Great job!</ListGroup.Item>
        </ListGroup>
      </Card>
    </div>
  );
}

export default Insights;
