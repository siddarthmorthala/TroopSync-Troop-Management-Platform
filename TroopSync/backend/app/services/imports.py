def parse_scoutbook_csv(rows: list[dict]) -> dict:
    return {"source": "Scoutbook", "rows_received": len(rows), "status": "parsed_demo"}

def parse_internet_advancement_csv(rows: list[dict]) -> dict:
    return {"source": "Internet Advancement", "rows_received": len(rows), "status": "parsed_demo"}
