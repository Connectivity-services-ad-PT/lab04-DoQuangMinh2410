from typing import Dict, Any

class PolicyEngine:
    def __init__(self):
        # Danh sách trắng giả lập các thẻ sinh viên CNTT 17-11 có quyền ra vào phòng server
        self.allowed_cards = {"card-12345678", "card-87654321", "card-24102004"}

    def evaluate_access(self, card_id: str, gate_id: str) -> Dict[str, Any]:
        """
        Hàm phân tích luật an ninh nghiệp vụ trung tâm
        """
        # Giả lập luật: Chỉ các thẻ nằm trong whitelist mới được vào các cổng khu vực Block D
        if card_id in self.allowed_cards:
            return {
                "status": "ALLOWED",
                "reason": f"Thẻ {card_id} hợp lệ. Đã xác thực quyền ra vào tại {gate_id}."
            }
        else:
            return {
                "status": "DENIED",
                "reason": f"Thẻ {card_id} không có trong danh sách phân quyền của hệ thống."
            }

policy_engine = PolicyEngine()