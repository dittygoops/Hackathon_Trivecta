const Stock = ({ name, description, risk_score, growth_potential }) => (
    <div className="stock">
        <h2>{name}</h2>
        <p>{description}</p>
        <p>Risk Score: {risk_score}</p>
        <p>Growth Potential: {growth_potential}</p>
    </div>
);

export default Stock;