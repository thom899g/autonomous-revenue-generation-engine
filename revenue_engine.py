from optimization_module import ModelOptimizer
from risk_assessment import RiskAssessor
from data_analyzer import DataAnalyzer
from dashboard_connector import DashboardConnector

class RevenueEngine:
    def __init__(self):
        self.optimizer = ModelOptimizer()
        self.risk_assessor = RiskAssessor()
        self.data_analyzer = DataAnalyzer()
        self.dashboard = DashboardConnector()
        
    def fetch_market_data(self):
        """Fetches current market data for analysis."""
        try:
            return self.data_analyzer.get_current_market_data()
        except Exception as e:
            print(f"Error fetching market data: {e}")
            return None
            
    def optimize_models(self, models):
        """Optimizes given business models using advanced algorithms."""
        try:
            return self.optimizer.optimize(models)
        except Exception as e:
            print(f"Optimization failed: {e}")
            return models
            
    def assess_risk(self, model):
        """Assesses the viability of a business model in the current market."""
        try:
            return self.risk_assessor.assess(model)
        except Exception as e:
            print(f"Risk assessment failed: {e}")
            return (False, str(e))
            
    def generate_report(self):
        """Generates comprehensive analysis reports for the dashboard."""
        data = self.data_analyzer.get_historical_data()
        optimized_models = self.optimize_models(data)
        risk_assessments = [self.assess_risk(model) for model in optimized_models]
        
        report = {
            'models': optimized_models,
            'risks': risk_assessments,
            'analysis': data
        }
        return report
        
    def trigger_actions(self, profitable_models):
        """Executes actions based on identified profitable models."""
        try:
            self.dashboard.update(proFITABLE_MODELS=profitable_models)
            print(f"Updated dashboard with {len(proFITABLE_MODELS)} profitable models.")
        except Exception as e:
            print(f"Failed to update dashboard: {e}")