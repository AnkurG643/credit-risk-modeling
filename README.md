# 📊 CreditVision: Credit Risk Assessment Tool

A machine learning-powered web application for assessing credit risk and calculating default probability based on various financial and personal factors.

## 🌟 Features

- **Real-time Risk Assessment**: Instant calculation of default probability
- **Credit Score Generation**: Automated credit scoring system
- **Credit Rating Assignment**: Letter grade rating (AAA to D)
- **Interactive Web Interface**: User-friendly Streamlit-based UI
- **Comprehensive Analysis**: Multiple risk factors consideration
- **Visual Risk Indicators**: Color-coded results with intuitive design

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone <your-repository-url>
cd creditvision
```

2. **Install required packages**
```bash
pip install streamlit pandas numpy scikit-learn
```

3. **Ensure prediction helper is available**
Make sure you have `prediction_helper.py` in the same directory with the `predict()` function implemented.

4. **Run the application**
```bash
streamlit run app.py
```

5. **Access the application**
Open your browser and navigate to `http://localhost:8501`

## 📋 Usage

### Input Parameters

The application requires the following information:

#### Personal Information
- **Age**: Applicant's age (18-100 years)
- **Residence Type**: Housing situation (Owned/Rented/Mortgage)
- **Open Loan Accounts**: Number of active loan accounts (1-4)

#### Financial Information
- **Annual Income**: Yearly income in Indian Rupees
- **Loan Amount**: Requested loan amount in Indian Rupees
- **Loan to Income Ratio**: Automatically calculated

#### Loan Details
- **Loan Purpose**: Education/Home/Auto/Personal
- **Loan Type**: Secured/Unsecured
- **Loan Tenure**: Repayment period in months

#### Credit History
- **Average DPD**: Average Days Past Due per delinquency
- **Delinquency Ratio**: Percentage of late payments
- **Credit Utilization Ratio**: Percentage of available credit used

### Output

The application provides:

1. **Default Probability** (0-100%)
   - 🟢 Low Risk: 0-20%
   - 🟡 Medium Risk: 20-50%
   - 🔴 High Risk: 50%+

2. **Credit Score** (300-850 range)
   - ⭐ Excellent: 750+
   - ⚠️ Good: 650-749
   - ❌ Poor: Below 650

3. **Credit Rating** (Letter grades)
   - AAA, AA, A: High grade
   - BBB, BB, B: Medium grade
   - CCC, CC, C, D: Low grade

## 🏗️ Project Structure

```
creditvision/
│
├── app.py                 # Main Streamlit application
├── prediction_helper.py   # ML model and prediction logic
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
└── data/                  # Training data (if applicable)
```

## 🔧 Technical Details

### Dependencies

- **Streamlit**: Web application framework
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **scikit-learn**: Machine learning library

### Model Information

- **Algorithm**: Ensemble machine learning methods
- **Training Data**: Historical financial and credit data
- **Features**: 11 key financial and personal attributes
- **Output**: Probability scores, credit ratings, and risk classifications

## 📊 Risk Assessment Methodology

The model considers multiple factors:

### Financial Factors (Weight: High)
- Income stability and amount
- Debt-to-income ratio
- Loan amount relative to income

### Credit History (Weight: High)
- Payment history and delinquencies
- Credit utilization patterns
- Account management behavior

### Personal Factors (Weight: Medium)
- Age and stability indicators
- Residence type and stability
- Loan purpose and type

## 🎨 User Interface Features

- **Responsive Design**: Works on desktop and mobile devices
- **Intuitive Layout**: Organized in logical sections and tabs
- **Visual Feedback**: Color-coded results and progress indicators
- **Interactive Elements**: Real-time calculations and updates
- **Professional Styling**: Modern gradient designs and clean typography

## ⚠️ Important Disclaimers

1. **Not Financial Advice**: This tool provides estimates only and should not be the sole basis for financial decisions
2. **Model Limitations**: Results are based on available data and model assumptions
3. **Regulatory Compliance**: Ensure compliance with local financial regulations
4. **Data Privacy**: Handle user data according to privacy laws and regulations

## 🔮 Future Enhancements

- [ ] Export results to PDF reports
- [ ] Historical tracking and trends
- [ ] Integration with credit bureaus
- [ ] Advanced model interpretability features
- [ ] Batch processing capabilities
- [ ] API endpoint development

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For questions or support:
- Create an issue in the GitHub repository
- Contact the development team
- Review the documentation and code comments

## 🏆 Acknowledgments

- Built with Streamlit for rapid web app development
- Machine learning models powered by scikit-learn
- UI design inspired by modern fintech applications

---

**Powered by Machine Learning • CreditVision Risk Assessment Tool**

*Version 1.0.0 - Built for accurate and efficient credit risk assessment*
