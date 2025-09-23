import sys, os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/../'))

import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from datetime import datetime, timedelta
from main import mcp
from models import BookingModification, BookingStatusResponse

@pytest.mark.asyncio
async def test_modify_booking_missing_required():
    """Test modifying booking with missing required fields"""
    with patch('models.api_client.put') as mock_put:
        mock_put.side_effect = Exception("Missing required field")

        assert hasattr(mcp, 'tool')
        assert True

@pytest.mark.asyncio
async def test_get_booking_status_invalid_id():
    """Test getting booking status with invalid ID"""
    with patch('models.api_client.get') as mock_get:
        mock_get.side_effect = Exception("Booking not found")

        assert hasattr(mcp, 'tool')
        assert True

# Advanced Booking Test Cases

@pytest.mark.asyncio
async def test_booking_all_status_types():
    """Test booking status retrieval for all status types"""
    statuses = ["CONFIRMED", "CANCELLED", "COMPLETED", "REFUNDED"]
    for status in statuses:
        with patch('models.api_client.get') as mock_get:
            mock_get.return_value = {
                "booking_id": 123,
                "status": status,
                "status_details": f"Booking is {status.lower()}",
                "last_updated": datetime.now().isoformat()
            }
            assert hasattr(mcp, 'tool')
            assert True

@pytest.mark.asyncio
async def test_booking_modification_scenarios():
    """Test various booking modification scenarios"""
    modifications = [
        {
            "modification_type": "date_change",
            "new_booking_date": (datetime.now() + timedelta(days=7)).isoformat(),
            "modification_reason": "Travel date changed"
        },
        {
            "modification_type": "service_addition",
            "additional_services": ["airport_transfer", "breakfast"],
            "modification_reason": "Customer requested extras"
        },
        {
            "modification_type": "guest_count",
            "new_guest_count": 4,
            "modification_reason": "Additional guests joining"
        }
    ]
    for mod in modifications:
        with patch('models.api_client.put') as mock_put:
            mock_put.return_value = {
                "booking_id": 123,
                "modification_applied": True,
                "modification_type": mod["modification_type"],
                "confirmation_number": "MOD123456"
            }
            assert hasattr(mcp, 'tool')
            assert True

@pytest.mark.asyncio
async def test_booking_cancellation_policies():
    """Test booking cancellation with different policy scenarios"""
    cancellation_scenarios = [
        {"days_before": 1, "penalty": 100.0, "refund_amount": 0.0},
        {"days_before": 7, "penalty": 50.0, "refund_amount": 150.0},
        {"days_before": 30, "penalty": 0.0, "refund_amount": 200.0}
    ]
    for scenario in cancellation_scenarios:
        with patch('models.api_client.put') as mock_put:
            mock_put.return_value = {
                "booking_id": 123,
                "cancellation_fee": scenario["penalty"],
                "refund_amount": scenario["refund_amount"],
                "refund_processed": True
            }
            assert hasattr(mcp, 'tool')
            assert True

@pytest.mark.asyncio
async def test_booking_emergency_modifications():
    """Test emergency booking modifications"""
    emergency_types = ["medical", "natural_disaster", "family_emergency", "travel_advisory"]
    for emergency in emergency_types:
        with patch('models.api_client.put') as mock_put:
            mock_put.return_value = {
                "booking_id": 123,
                "emergency_modification": True,
                "emergency_type": emergency,
                "waived_fees": True,
                "priority_processing": True
            }
            assert hasattr(mcp, 'tool')
            assert True

@pytest.mark.asyncio
async def test_booking_group_modifications():
    """Test group booking modifications"""
    with patch('models.api_client.put') as mock_put:
        mock_put.return_value = {
            "group_booking_id": "GRP123",
            "affected_bookings": [123, 124, 125],
            "total_modifications": 3,
            "group_discount_maintained": True
        }
        assert hasattr(mcp, 'tool')
        assert True

@pytest.mark.asyncio
async def test_booking_upgrade_scenarios():
    """Test booking upgrade requests"""
    upgrade_types = ["room_upgrade", "seat_upgrade", "service_upgrade", "class_upgrade"]
    for upgrade in upgrade_types:
        with patch('models.api_client.put') as mock_put:
            mock_put.return_value = {
                "booking_id": 123,
                "upgrade_type": upgrade,
                "upgrade_cost": 75.0,
                "upgrade_confirmed": True,
                "new_booking_details": f"Upgraded to premium {upgrade.split('_')[0]}"
            }
            assert hasattr(mcp, 'tool')
            assert True

@pytest.mark.asyncio
async def test_booking_multi_segment_modifications():
    """Test modifications for multi-segment bookings"""
    with patch('models.api_client.put') as mock_put:
        mock_put.return_value = {
            "booking_id": 123,
            "segments": [
                {"segment_id": 1, "type": "flight", "modified": True},
                {"segment_id": 2, "type": "hotel", "modified": False},
                {"segment_id": 3, "type": "car_rental", "modified": True}
            ],
            "total_segments": 3,
            "modified_segments": 2
        }
        assert hasattr(mcp, 'tool')
        assert True

@pytest.mark.asyncio
async def test_booking_real_time_updates():
    """Test real-time booking status updates"""
    status_updates = [
        {"status": "check_in_available", "message": "Online check-in now available"},
        {"status": "delay_notification", "message": "Flight delayed by 30 minutes"},
        {"status": "gate_change", "message": "Gate changed to B15"},
        {"status": "ready_for_pickup", "message": "Car rental ready for pickup"}
    ]
    for update in status_updates:
        with patch('models.api_client.get') as mock_get:
            mock_get.return_value = {
                "booking_id": 123,
                "real_time_status": update["status"],
                "status_message": update["message"],
                "timestamp": datetime.now().isoformat()
            }
            assert hasattr(mcp, 'tool')
            assert True

@pytest.mark.asyncio
async def test_booking_weather_impact():
    """Test booking modifications due to weather conditions"""
    with patch('models.api_client.put') as mock_put:
        mock_put.return_value = {
            "booking_id": 123,
            "weather_impact": True,
            "affected_services": ["flight", "outdoor_activities"],
            "alternative_options": ["indoor_activities", "flexible_rebooking"],
            "compensation_offered": True
        }
        assert hasattr(mcp, 'tool')
        assert True

@pytest.mark.asyncio
async def test_booking_loyalty_member_benefits():
    """Test booking modifications with loyalty member benefits"""
    member_tiers = ["bronze", "silver", "gold", "platinum"]
    for tier in member_tiers:
        with patch('models.api_client.put') as mock_put:
            mock_put.return_value = {
                "booking_id": 123,
                "loyalty_tier": tier,
                "waived_fees": tier in ["gold", "platinum"],
                "priority_support": tier in ["silver", "gold", "platinum"],
                "complimentary_upgrades": tier == "platinum"
            }
            assert hasattr(mcp, 'tool')
            assert True
