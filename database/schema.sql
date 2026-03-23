CREATE TABLE signals (
    id INTEGER PRIMARY KEY,
    subject_id INTEGER,
    signal_path TEXT,
    signal_type TEXT,
    label TEXT,
    created_at TEXT
);

CREATE TABLE inference_logs (
    id INTEGER PRIMARY KEY,
    signal_id INTEGER,
    request_payload TEXT,
    prediction TEXT,
    latency_ms REAL,
    created_at TEXT
);

CREATE TABLE IF NOT EXISTS inference_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    input TEXT,
    prediction TEXT,
    latency_ms REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);