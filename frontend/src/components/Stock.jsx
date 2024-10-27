import './Stock.css';

const Stock = ({ ticker, description, risk_score, growth_potential, isSelected, onClick }) => (
    <div className={`stock ${isSelected ? 'selected' : ''}`} onClick={onClick}>
        <div className='abc'>
            <div>{ticker}</div>
            <div>{risk_score}</div>
            <div>{growth_potential}</div>
        </div>
        <div>{description}</div>
    </div>
);

export default Stock;
