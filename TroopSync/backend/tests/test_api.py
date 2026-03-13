from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json()['status'] == 'ok'


def test_advancement_rules_reject_overflow():
    r = client.post('/advancement/check', json={"completed_requirements": 8, "total_requirements": 7})
    assert r.status_code == 200
    assert r.json()['valid'] is False


def test_ledger_summary_balances():
    client.post('/ledger', json={"entry_type": "credit", "amount": 100.0, "description": "Fundraiser"})
    client.post('/ledger', json={"entry_type": "debit", "amount": 40.0, "description": "Camp food"})
    r = client.get('/ledger/summary')
    assert r.status_code == 200
    assert r.json()['net_balance'] == 60.0
