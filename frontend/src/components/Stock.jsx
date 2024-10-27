import './Stock.css';

const Stock = ({ ticker, description, risk_score, growth_potential, isSelected, onClick }) => (
    <div className={`stock ${isSelected ? 'selected' : ''}`} onClick={onClick}>
        <div className='top-row'>
            <div>{ticker}</div>
            <div>{growth_potential}</div>
            <div>{risk_score}</div>
        </div>
        <div className='description'>{description}</div>
    </div>
);

export default Stock;
