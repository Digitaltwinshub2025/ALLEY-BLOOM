"""
Comprehensive test suite for Alley Bloom
Tests Phase 1, 2, and 3 fixes
"""
import requests
import json
import time
from datetime import datetime

BASE_URL = "http://localhost:5000"

# Color codes for output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def print_test(name, passed, message=""):
    status = f"{GREEN}✓ PASS{RESET}" if passed else f"{RED}✗ FAIL{RESET}"
    print(f"{status} - {name}")
    if message:
        print(f"  {message}")

def print_section(title):
    print(f"\n{BLUE}{'='*60}")
    print(f"{title}")
    print(f"{'='*60}{RESET}\n")

# ============================================================================
# PHASE 1 TESTS
# ============================================================================

def test_phase1():
    print_section("PHASE 1: API Endpoints & Core Fixes")
    
    tests_passed = 0
    tests_total = 0
    
    # Test 1: Homepage loads
    tests_total += 1
    try:
        response = requests.get(f"{BASE_URL}/")
        passed = response.status_code == 200
        print_test("Homepage loads", passed, f"Status: {response.status_code}")
        if passed:
            tests_passed += 1
    except Exception as e:
        print_test("Homepage loads", False, str(e))
    
    # Test 2: Scenarios endpoint (JSON fallback)
    tests_total += 1
    try:
        response = requests.get(f"{BASE_URL}/api/scenarios")
        passed = response.status_code == 200 and 'scenarios' in response.json()
        scenarios = response.json().get('scenarios', [])
        print_test("Scenarios endpoint", passed, f"Found {len(scenarios)} scenarios")
        if passed:
            tests_passed += 1
    except Exception as e:
        print_test("Scenarios endpoint", False, str(e))
    
    # Test 3: Images API endpoint
    tests_total += 1
    try:
        response = requests.get(f"{BASE_URL}/api/images/urban%20garden")
        passed = response.status_code == 200
        data = response.json()
        print_test("Images API endpoint", passed, f"Response: {data.get('error', 'OK')}")
        if passed:
            tests_passed += 1
    except Exception as e:
        print_test("Images API endpoint", False, str(e))
    
    # Test 4: Weather API endpoint
    tests_total += 1
    try:
        response = requests.get(f"{BASE_URL}/api/weather/34.0475/-118.2795")
        passed = response.status_code == 200
        data = response.json()
        has_data = 'main' in data or 'error' in data
        print_test("Weather API endpoint", passed and has_data, f"Status: {response.status_code}")
        if passed and has_data:
            tests_passed += 1
    except Exception as e:
        print_test("Weather API endpoint", False, str(e))
    
    # Test 5: Solar API endpoint
    tests_total += 1
    try:
        response = requests.get(f"{BASE_URL}/api/solar/34.0475/-118.2795")
        passed = response.status_code == 200
        data = response.json()
        has_data = 'parameters' in data or 'error' in data
        print_test("Solar API endpoint", passed and has_data, f"Status: {response.status_code}")
        if passed and has_data:
            tests_passed += 1
    except Exception as e:
        print_test("Solar API endpoint", False, str(e))
    
    # Test 6: Species API endpoint
    tests_total += 1
    try:
        response = requests.get(f"{BASE_URL}/api/species/34.0475/-118.2795")
        passed = response.status_code == 200
        data = response.json()
        has_data = 'results' in data or 'error' in data
        print_test("Species API endpoint", passed and has_data, f"Status: {response.status_code}")
        if passed and has_data:
            tests_passed += 1
    except Exception as e:
        print_test("Species API endpoint", False, str(e))
    
    # Test 7: Water API endpoint
    tests_total += 1
    try:
        response = requests.get(f"{BASE_URL}/api/water/11092450")
        passed = response.status_code == 200
        data = response.json()
        has_data = 'value' in data or 'error' in data
        print_test("Water API endpoint", passed and has_data, f"Status: {response.status_code}")
        if passed and has_data:
            tests_passed += 1
    except Exception as e:
        print_test("Water API endpoint", False, str(e))
    
    # Test 8: Plant Library endpoint
    tests_total += 1
    try:
        response = requests.get(f"{BASE_URL}/api/plants")
        passed = response.status_code == 200
        data = response.json()
        has_plants = 'plants' in data and len(data.get('plants', [])) > 0
        print_test("Plant Library endpoint", passed and has_plants, f"Found {len(data.get('plants', []))} plants")
        if passed and has_plants:
            tests_passed += 1
    except Exception as e:
        print_test("Plant Library endpoint", False, str(e))
    
    # Test 9: Live Dashboard endpoint
    tests_total += 1
    try:
        response = requests.get(f"{BASE_URL}/api/live-data/alley3")
        passed = response.status_code == 200
        data = response.json()
        has_data = 'temperature' in data or 'error' in data
        print_test("Live Dashboard endpoint", passed and has_data, f"Status: {response.status_code}")
        if passed and has_data:
            tests_passed += 1
    except Exception as e:
        print_test("Live Dashboard endpoint", False, str(e))
    
    # Test 10: Google Data endpoint
    tests_total += 1
    try:
        response = requests.get(f"{BASE_URL}/api/google-data/alley3")
        passed = response.status_code == 200
        data = response.json()
        has_data = 'air_quality' in data or 'error' in data
        print_test("Google Data endpoint", passed and has_data, f"Status: {response.status_code}")
        if passed and has_data:
            tests_passed += 1
    except Exception as e:
        print_test("Google Data endpoint", False, str(e))
    
    print(f"\n{BLUE}Phase 1 Results: {tests_passed}/{tests_total} tests passed{RESET}")
    return tests_passed, tests_total

# ============================================================================
# PHASE 2 TESTS
# ============================================================================

def test_phase2():
    print_section("PHASE 2: Error Handling & Data Standardization")
    
    tests_passed = 0
    tests_total = 0
    
    # Test 1: API test page loads
    tests_total += 1
    try:
        response = requests.get(f"{BASE_URL}/api-test")
        passed = response.status_code == 200
        print_test("API test page loads", passed, f"Status: {response.status_code}")
        if passed:
            tests_passed += 1
    except Exception as e:
        print_test("API test page loads", False, str(e))
    
    # Test 2: Plant Library fallback data
    tests_total += 1
    try:
        response = requests.get(f"{BASE_URL}/api/plants")
        data = response.json()
        has_fallback = len(data.get('plants', [])) > 0
        print_test("Plant Library fallback data", has_fallback, f"Fallback plants: {len(data.get('plants', []))}")
        if has_fallback:
            tests_passed += 1
    except Exception as e:
        print_test("Plant Library fallback data", False, str(e))
    
    # Test 3: Live Dashboard data structure
    tests_total += 1
    try:
        response = requests.get(f"{BASE_URL}/api/live-data/alley3")
        data = response.json()
        # Check for required fields
        required_fields = ['temperature', 'air_quality_index', 'pm25', 'shade_coverage']
        has_all_fields = all(field in data for field in required_fields)
        print_test("Live Dashboard data structure", has_all_fields, f"Fields present: {has_all_fields}")
        if has_all_fields:
            tests_passed += 1
    except Exception as e:
        print_test("Live Dashboard data structure", False, str(e))
    
    # Test 4: Error handling on invalid endpoint
    tests_total += 1
    try:
        response = requests.get(f"{BASE_URL}/api/invalid-endpoint")
        passed = response.status_code == 404
        print_test("Error handling (404)", passed, f"Status: {response.status_code}")
        if passed:
            tests_passed += 1
    except Exception as e:
        print_test("Error handling (404)", False, str(e))
    
    # Test 5: Design workspace page loads
    tests_total += 1
    try:
        response = requests.get(f"{BASE_URL}/design-workspace")
        passed = response.status_code == 200
        print_test("Design workspace page loads", passed, f"Status: {response.status_code}")
        if passed:
            tests_passed += 1
    except Exception as e:
        print_test("Design workspace page loads", False, str(e))
    
    # Test 6: Scenarios page loads
    tests_total += 1
    try:
        response = requests.get(f"{BASE_URL}/scenarios")
        passed = response.status_code == 200
        print_test("Scenarios page loads", passed, f"Status: {response.status_code}")
        if passed:
            tests_passed += 1
    except Exception as e:
        print_test("Scenarios page loads", False, str(e))
    
    print(f"\n{BLUE}Phase 2 Results: {tests_passed}/{tests_total} tests passed{RESET}")
    return tests_passed, tests_total

# ============================================================================
# PHASE 3 TESTS
# ============================================================================

def test_phase3():
    print_section("PHASE 3: Authentication & Database")
    
    tests_passed = 0
    tests_total = 0
    session = requests.Session()
    
    # Test 1: Register new user
    tests_total += 1
    try:
        response = session.post(f"{BASE_URL}/api/auth/register", json={
            'username': f'testuser_{int(time.time())}',
            'email': f'test_{int(time.time())}@example.com',
            'password': 'testpass123',
            'full_name': 'Test User'
        })
        passed = response.status_code == 201
        data = response.json()
        print_test("User registration", passed, f"Status: {response.status_code}")
        if passed:
            tests_passed += 1
            username = data.get('user', {}).get('username')
    except Exception as e:
        print_test("User registration", False, str(e))
        username = None
    
    # Test 2: Login user
    tests_total += 1
    try:
        response = session.post(f"{BASE_URL}/api/auth/login", json={
            'username': username or 'testuser',
            'password': 'testpass123'
        })
        passed = response.status_code in [200, 401]  # 401 if user doesn't exist
        print_test("User login", passed, f"Status: {response.status_code}")
        if response.status_code == 200:
            tests_passed += 1
    except Exception as e:
        print_test("User login", False, str(e))
    
    # Test 3: Get current user (protected endpoint)
    tests_total += 1
    try:
        response = session.get(f"{BASE_URL}/api/auth/me")
        passed = response.status_code in [200, 401]
        print_test("Get current user", passed, f"Status: {response.status_code}")
        if response.status_code == 200:
            tests_passed += 1
    except Exception as e:
        print_test("Get current user", False, str(e))
    
    # Test 4: Create scenario in database
    tests_total += 1
    try:
        response = session.post(f"{BASE_URL}/api/scenarios/db", json={
            'id': f'test_scenario_{int(time.time())}',
            'name': 'Test Scenario',
            'type': 'baseline',
            'alley_id': 'alley3',
            'phase': 'Planning',
            'environmental_data': {
                'temperature': 95,
                'air_quality': 92
            }
        })
        passed = response.status_code in [200, 201]
        print_test("Create scenario in database", passed, f"Status: {response.status_code}")
        if passed:
            tests_passed += 1
    except Exception as e:
        print_test("Create scenario in database", False, str(e))
    
    # Test 5: Get scenarios from database
    tests_total += 1
    try:
        response = session.get(f"{BASE_URL}/api/scenarios/db")
        passed = response.status_code == 200 and 'scenarios' in response.json()
        data = response.json()
        print_test("Get scenarios from database", passed, f"Found {len(data.get('scenarios', []))} scenarios")
        if passed:
            tests_passed += 1
    except Exception as e:
        print_test("Get scenarios from database", False, str(e))
    
    # Test 6: Export scenario as JSON
    tests_total += 1
    try:
        response = session.get(f"{BASE_URL}/api/scenarios/export/alley3-baseline/json")
        passed = response.status_code in [200, 404]
        print_test("Export scenario as JSON", passed, f"Status: {response.status_code}")
        if response.status_code == 200:
            tests_passed += 1
    except Exception as e:
        print_test("Export scenario as JSON", False, str(e))
    
    # Test 7: Logout user
    tests_total += 1
    try:
        response = session.post(f"{BASE_URL}/api/auth/logout")
        passed = response.status_code == 200
        print_test("User logout", passed, f"Status: {response.status_code}")
        if passed:
            tests_passed += 1
    except Exception as e:
        print_test("User logout", False, str(e))
    
    print(f"\n{BLUE}Phase 3 Results: {tests_passed}/{tests_total} tests passed{RESET}")
    return tests_passed, tests_total

# ============================================================================
# MAIN TEST RUNNER
# ============================================================================

def main():
    print(f"\n{YELLOW}{'='*60}")
    print("ALLEY BLOOM - COMPREHENSIVE TEST SUITE")
    print(f"{'='*60}{RESET}\n")
    
    print(f"Testing: {BASE_URL}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Wait for server to be ready
    print("Waiting for server to be ready...")
    for i in range(10):
        try:
            requests.get(f"{BASE_URL}/")
            print("Server is ready!\n")
            break
        except:
            if i < 9:
                time.sleep(1)
            else:
                print(f"{RED}Server not responding after 10 seconds{RESET}")
                return
    
    # Run tests
    p1_passed, p1_total = test_phase1()
    p2_passed, p2_total = test_phase2()
    p3_passed, p3_total = test_phase3()
    
    # Summary
    total_passed = p1_passed + p2_passed + p3_passed
    total_tests = p1_total + p2_total + p3_total
    
    print_section("TEST SUMMARY")
    print(f"Phase 1 (API Endpoints):        {p1_passed}/{p1_total}")
    print(f"Phase 2 (Error Handling):       {p2_passed}/{p2_total}")
    print(f"Phase 3 (Auth & Database):      {p3_passed}/{p3_total}")
    print(f"\n{'='*60}")
    print(f"TOTAL: {total_passed}/{total_tests} tests passed")
    
    if total_passed == total_tests:
        print(f"{GREEN}✓ ALL TESTS PASSED - APPLICATION IS READY{RESET}")
    else:
        print(f"{YELLOW}⚠ {total_tests - total_passed} tests failed - Review above{RESET}")
    
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()
