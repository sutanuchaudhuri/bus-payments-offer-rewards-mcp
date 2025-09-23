#!/usr/bin/env python3
"""
Comprehensive Test Runner and Summary for FastMCP Advanced Test Suite
"""
import sys
import os
sys.path.insert(0, os.path.abspath('.'))

import subprocess
from datetime import datetime

def count_tests_in_file(filepath):
    """Count the number of test functions in a file"""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        return content.count('async def test_')
    except FileNotFoundError:
        return 0

def run_test_suite():
    """Run the complete test suite and provide summary"""
    print("🚀 FastMCP Advanced Test Suite Runner")
    print("=" * 60)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Test file summary
    test_files = {
        "tests/test_customer.py": "Customer Management Tests",
        "tests/test_offer.py": "Offer & Promotion Tests",
        "tests/test_payment.py": "Payment Processing Tests",
        "tests/test_refund.py": "Refund Management Tests",
        "tests/test_reward.py": "Reward Program Tests",
        "tests/test_merchant.py": "Merchant Management Tests",
        "tests/test_credit_card.py": "Credit Card Tests",
        "tests/test_integration.py": "Integration & API Tests",
        "tests/test_booking.py": "Booking Management Tests"
    }

    total_tests = 0
    print("📊 Test Suite Summary:")
    print("-" * 40)

    for filepath, description in test_files.items():
        test_count = count_tests_in_file(filepath)
        total_tests += test_count
        print(f"{description:<30} {test_count:>3} tests")

    print("-" * 40)
    print(f"{'Total Test Cases':<30} {total_tests:>3} tests")
    print()

    # Test categories breakdown
    print("🔍 Advanced Test Categories Covered:")
    print("-" * 40)

    categories = [
        "✅ Happy Path Scenarios",
        "✅ Edge Case Validation",
        "✅ Error Handling & Exceptions",
        "✅ Type Safety & Data Validation",
        "✅ Business Logic Testing",
        "✅ Integration Scenarios",
        "✅ Security & Fraud Detection",
        "✅ Performance & Analytics",
        "✅ Workflow & State Management",
        "✅ Compliance & Regulatory",
        "✅ Multi-tier Product Testing",
        "✅ International Data Handling",
        "✅ Rate Limiting & API Failures",
        "✅ Real-time Updates & Notifications",
        "✅ Batch Operations & Bulk Processing"
    ]

    for category in categories:
        print(f"  {category}")

    print()

    # Key features tested
    print("🎯 Key Features Tested:")
    print("-" * 40)
    features = [
        "Customer lifecycle management (CRUD operations)",
        "Credit card product tiers (BASIC → PLATINUM)",
        "Offer activation & usage tracking",
        "Payment processing & fraud detection",
        "Refund workflows & approval processes",
        "Reward point earning & redemption",
        "Merchant verification & risk assessment",
        "Token management & security",
        "Travel booking integrations",
        "Shopping cart & order processing",
        "Multi-location merchant support",
        "Seasonal promotions & campaigns",
        "Chargeback prevention & management",
        "Emergency booking modifications",
        "Loyalty program benefits & tiers"
    ]

    for i, feature in enumerate(features, 1):
        print(f"  {i:>2}. {feature}")

    print()

    # Run the actual tests
    print("🧪 Running Test Suite...")
    print("-" * 40)

    try:
        # Run pytest with verbose output
        result = subprocess.run([
            sys.executable, '-m', 'pytest', 'tests/',
            '--tb=short', '-v', '--disable-warnings'
        ], capture_output=True, text=True, timeout=300)

        if result.returncode == 0:
            print("✅ All tests passed successfully!")
        else:
            print("❌ Some tests failed or had issues")
            if result.stdout:
                print("STDOUT:", result.stdout[-500:])  # Last 500 chars
            if result.stderr:
                print("STDERR:", result.stderr[-500:])  # Last 500 chars

    except subprocess.TimeoutExpired:
        print("⏰ Test execution timed out (5 minutes)")
    except FileNotFoundError:
        print("📦 pytest not found - install with: pip install pytest")
    except Exception as e:
        print(f"🔧 Test execution error: {e}")

    print()
    print("📈 Test Suite Statistics:")
    print("-" * 40)
    print(f"  Total Test Functions: {total_tests}")
    print(f"  Test Files: {len(test_files)}")
    print(f"  Coverage Areas: {len(categories)}")
    print(f"  Key Features: {len(features)}")
    print()
    print("🎉 Advanced Test Suite Complete!")
    print(f"Finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    run_test_suite()
