import React from "react";
import { Card, Row, Col } from "react-bootstrap";

function Dashboard() {
  return (
    <div className="content">
      <h2 style={{ color: 'var(--dark-bg)' }}>Dashboard</h2>
      {/* <Row>
        <Col>
          <Card className="text-center">
            <Card.Body>
              <Card.Title>Daily Food Waste</Card.Title>
              <Card.Text>50kg</Card.Text>
            </Card.Body>
          </Card>
        </Col>
        <Col>
          <Card className="text-center">
            <Card.Body>
              <Card.Title>Surplus Redistributed</Card.Title>
              <Card.Text>30kg</Card.Text>
            </Card.Body>
          </Card>
        </Col>
        <Col>
          <Card className="text-center">
            <Card.Body>
              <Card.Title>Food Utilization Rate</Card.Title>
              <Card.Text>85%</Card.Text>
            </Card.Body>
          </Card>
        </Col>
      </Row> */}
      {/* Add charts here using Chart.js or Plotly */}
    </div>  
  );
}

export default Dashboard;
