import streamlit as st
from prediction_helper import predict  # Ensure this is correctly linked to your prediction_helper.py

# Set the page configuration and title
st.set_page_config(
    page_title="CreditVision: Credit Risk Modelling", 
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 2rem;
        padding: 1rem;
        background: linear-gradient(90deg, #f0f8ff, #e6f3ff);
        border-radius: 10px;
        border: 2px solid #1f77b4;
    }
    
    .section-header {
        color: #2c3e50;
        font-size: 1.3rem;
        font-weight: bold;
        margin: 1.5rem 0 1rem 0;
        padding: 0.5rem 0;
        border-bottom: 2px solid #3498db;
    }
    
    .metric-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #3498db;
        margin: 0.5rem 0;
    }
    
    .result-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        text-align: center;
        color: white;
    }
    
    .result-value {
        font-size: 2rem;
        font-weight: bold;
        margin: 0.5rem 0;
    }
    
    .calculate-btn {
        background: linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%);
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        color: white;
        font-size: 1.2rem;
        font-weight: bold;
        cursor: pointer;
        width: 100%;
        margin: 2rem 0;
    }
    
    .info-box {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #2196F3;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<div class="main-header">📊 CreditVision: Credit Risk Assessment</div>', unsafe_allow_html=True)

# Add description
st.markdown("""
<div class="info-box">
    <strong>ℹ️ About this tool:</strong> This application uses machine learning to assess credit risk and calculate 
    default probability based on various financial and personal factors. Fill in the details below to get an instant risk assessment.
</div>
""", unsafe_allow_html=True)

# Create tabs for better organization
tab1, tab2 = st.tabs(["📋 Risk Assessment", "📊 About the Model"])

with tab1:
    # Personal Information Section
    st.markdown('<div class="section-header">👤 Personal Information</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('🎂 Age', min_value=18, step=1, max_value=100, value=28, 
                             help="Applicant's age in years")
    with col2:
        residence_type = st.selectbox('🏠 Residence Type', ['Owned', 'Rented', 'Mortgage'],
                                     help="Current housing situation")
    with col3:
        num_open_accounts = st.number_input('💳 Open Loan Accounts', min_value=1, max_value=4, step=1, value=2,
                                           help="Number of currently active loan accounts")

    # Financial Information Section
    st.markdown('<div class="section-header">💰 Financial Information</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        income = st.number_input('💵 Annual Income (₹)', min_value=0, value=1200000, step=10000,
                                format="%d", help="Annual income in Indian Rupees")
    with col2:
        loan_amount = st.number_input('🏦 Loan Amount (₹)', min_value=0, value=2560000, step=10000,
                                     format="%d", help="Requested loan amount in Indian Rupees")
    with col3:
        # Calculate and display Loan to Income Ratio
        loan_to_income_ratio = loan_amount / income if income > 0 else 0
        st.markdown(f"""
        <div class="metric-card">
            <strong>📊 Loan to Income Ratio</strong><br>
            <span style="font-size: 1.5rem; color: #e74c3c; font-weight: bold;">{loan_to_income_ratio:.2f}</span>
            <br><small>{"⚠️ High Risk" if loan_to_income_ratio > 3 else "✅ Normal" if loan_to_income_ratio > 2 else "🟢 Low Risk"}</small>
        </div>
        """, unsafe_allow_html=True)

    # Loan Details Section
    st.markdown('<div class="section-header">📋 Loan Details</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        loan_purpose = st.selectbox('🎯 Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'],
                                   help="Purpose for taking the loan")
    with col2:
        loan_type = st.selectbox('🔒 Loan Type', ['Unsecured', 'Secured'],
                                help="Whether the loan is secured by collateral")
    with col3:
        loan_tenure_months = st.number_input('📅 Loan Tenure (months)', min_value=0, step=1, value=36,
                                            help="Loan repayment period in months")

    # Credit History Section
    st.markdown('<div class="section-header">📈 Credit History</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        avg_dpd_per_delinquency = st.number_input('⏰ Average DPD', min_value=0, value=20,
                                                 help="Average Days Past Due per delinquency")
    with col2:
        delinquency_ratio = st.number_input('📉 Delinquency Ratio (%)', min_value=0, max_value=100, step=1, value=30,
                                           help="Percentage of payments that were late")
    with col3:
        credit_utilization_ratio = st.number_input('💳 Credit Utilization Ratio (%)', min_value=0, max_value=100, 
                                                  step=1, value=30, help="Percentage of available credit being used")

    # Add some spacing
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Center the button using columns
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        calculate_button = st.button('🚀 Calculate Credit Risk', type="primary", use_container_width=True)

    # Results section
    if calculate_button:
        with st.spinner('Analyzing credit risk... 🔄'):
            probability, credit_score, rating = predict(age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
                                                       delinquency_ratio, credit_utilization_ratio, num_open_accounts,
                                                       residence_type, loan_purpose, loan_type)
        
        # Display results in attractive cards
        st.markdown('<div class="section-header">📊 Risk Assessment Results</div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # Risk level color coding
            if probability < 0.2:
                risk_color = "#27ae60"  # Green
                risk_emoji = "🟢"
                risk_level = "Low Risk"
            elif probability < 0.5:
                risk_color = "#f39c12"  # Orange
                risk_emoji = "🟡"
                risk_level = "Medium Risk"
            else:
                risk_color = "#e74c3c"  # Red
                risk_emoji = "🔴"
                risk_level = "High Risk"
            
            st.markdown(f"""
            <div style="background-color: {risk_color}; padding: 1.5rem; border-radius: 15px; text-align: center; color: white;">
                <h3>Default Probability</h3>
                <div style="font-size: 2.5rem; font-weight: bold;">{probability:.1%}</div>
                <div style="font-size: 1.2rem;">{risk_emoji} {risk_level}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Credit score color coding
            if credit_score >= 750:
                score_color = "#27ae60"
                score_emoji = "⭐"
            elif credit_score >= 650:
                score_color = "#f39c12"
                score_emoji = "⚠️"
            else:
                score_color = "#e74c3c"
                score_emoji = "❌"
            
            st.markdown(f"""
            <div style="background-color: {score_color}; padding: 1.5rem; border-radius: 15px; text-align: center; color: white;">
                <h3>Credit Score</h3>
                <div style="font-size: 2.5rem; font-weight: bold;">{credit_score}</div>
                <div style="font-size: 1.2rem;">{score_emoji} Score</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            # Rating color coding
            rating_colors = {
                'AAA': '#27ae60', 'AA': '#2ecc71', 'A': '#3498db',
                'BBB': '#f39c12', 'BB': '#e67e22', 'B': '#e74c3c',
                'CCC': '#c0392b', 'CC': '#a93226', 'C': '#922b21', 'D': '#7b241c'
            }
            rating_color = rating_colors.get(rating, '#95a5a6')
            
            st.markdown(f"""
            <div style="background-color: {rating_color}; padding: 1.5rem; border-radius: 15px; text-align: center; color: white;">
                <h3>Credit Rating</h3>
                <div style="font-size: 2.5rem; font-weight: bold;">{rating}</div>
                <div style="font-size: 1.2rem;">🏆 Grade</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Add interpretation
        st.markdown("---")
        st.markdown("### 📝 Interpretation Guide")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Default Probability:**
            - 🟢 Low (0-20%): Excellent creditworthiness
            - 🟡 Medium (20-50%): Moderate risk
            - 🔴 High (50%+): High risk of default
            """)
        
        with col2:
            st.markdown("""
            **Credit Score Range:**
            - ⭐ 750+: Excellent credit
            - ⚠️ 650-749: Good credit
            - ❌ Below 650: Poor credit
            """)

with tab2:
    st.markdown('<div class="section-header">🤖 About the Model</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🎯 Model Features
        - **Machine Learning Algorithm**: Advanced ensemble methods
        - **Key Factors**: Income, loan amount, credit history, demographics
        - **Output**: Probability score, credit rating, and risk assessment
        - **Accuracy**: Trained on historical financial data
        """)
        
    with col2:
        st.markdown("""
        ### 📊 Risk Factors Considered
        - **Financial**: Income, loan amount, debt-to-income ratio
        - **Credit History**: Past delinquencies, credit utilization
        - **Personal**: Age, residence type, loan purpose
        - **Account Info**: Number of open accounts, loan tenure
        """)
    
    st.markdown("""
    ### ⚠️ Disclaimer
    This tool provides estimates based on machine learning models and should not be the sole basis for financial decisions. 
    Always consult with financial advisors for comprehensive credit assessment.
    """)

# Footer
st.markdown("---")
st.markdown(
    '<div style="text-align: center; color: #7f8c8d; font-style: italic;">Powered by Machine Learning • CreditVision: Risk Assessment Tool</div>', 
    unsafe_allow_html=True
)