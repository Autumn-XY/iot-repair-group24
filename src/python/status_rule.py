"""Complete the two allowed work-order transitions."""

def can_transition(current, target):
    # 规则1：待处理 -> 处理中
    if current == "PENDING" and target == "PROCESSING":
        return True
        
    # 规则2：处理中 -> 已完成
    if current == "PROCESSING" and target == "COMPLETED":
        return True
        
    # 其余所有情况一律拒绝（包括跳级和回退）
    return False