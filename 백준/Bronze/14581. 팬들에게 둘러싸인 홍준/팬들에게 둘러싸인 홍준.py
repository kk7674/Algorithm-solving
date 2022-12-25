def surrounded_by_fans(hongjoon):
    base = [[":fan:" for _ in range(3)] for _ in range(3)]
    
    base[1][1] = f":{hongjoon}:"
    
    answer = "\n".join(["".join(ans) for ans in base])
    
    return answer


if __name__ == "__main__":
    hongjoon = input()
    
    print(surrounded_by_fans(hongjoon))