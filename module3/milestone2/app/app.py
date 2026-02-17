from typing import Any, Dict

def predict(payload: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(payload, dict):
        raise TypeError("payload must be a dict")

    if "text" not in payload:
        raise ValueError("Missing required field: text")

    text = payload["text"]
    if not isinstance(text, str) or not text.strip():
        raise ValueError("text must be a non-empty string")

    return {"label": "OK", "length": len(text)}

if __name__ == "__main__":
    print(predict({"text": "hello"}))
