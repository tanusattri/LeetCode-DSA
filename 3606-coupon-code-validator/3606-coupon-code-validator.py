class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        priority= {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }
        valid_coupons= []
        for i in range(len(code)):
            c= code[i]
            bl= businessLine[i]
            active= isActive[i]
            if not active:
                continue
            if bl not in priority:
                continue
            if not c:
                continue
            is_valid_code= True
            for char in c:
                if not (char.isalnum() or char == '_'):
                    is_valid_code= False
                    break
            if is_valid_code:
                valid_coupons.append((priority[bl], c))
        valid_coupons.sort()
        return [coupon[1] for coupon in valid_coupons]