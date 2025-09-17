def is_win(game):
    """
    检查游戏是否有获胜者
    参数: game - 3x3的游戏棋盘
    返回: True如果有获胜者，False否则
    """
    # 检查行
    for row in game:
        if row[0] == row[1] == row[2] and row[0] in ['X', 'O']:
            return True
    
    # 检查列
    for col in range(3):
        if game[0][col] == game[1][col] == game[2][col] and game[0][col] in ['X', 'O']:
            return True
    
    # 检查对角线
    if game[0][0] == game[1][1] == game[2][2] and game[0][0] in ['X', 'O']:
        return True
    if game[0][2] == game[1][1] == game[2][0] and game[0][2] in ['X', 'O']:
        return True
    
    return False

def get_valid_input(game):
    """
    获取有效的用户输入
    参数: game - 当前游戏棋盘
    返回: (i, j) - 有效的行列坐标
    """
    while True:
        try:
            print("请输入要标记的位置 (行 列)，例如：1 2")
            user_input = input("输入坐标 [1-3] [1-3]: ").strip()
            
            if not user_input:
                print("❌ 输入不能为空！请重新输入。")
                continue
                
            parts = user_input.split()
            if len(parts) != 2:
                print("❌ 请输入两个数字，用空格分隔！")
                continue
                
            i, j = map(int, parts)
            i -= 1  # 转换为0-2的索引
            j -= 1
            
            # 检查范围
            if not (0 <= i < 3 and 0 <= j < 3):
                print("❌ 坐标超出范围！请输入1-3之间的数字。")
                continue
            
            # 检查位置是否已被占用
            if game[i][j] != ' ':
                print("❌ 该位置已被占用！请选择其他位置。")
                continue
            
            return i, j
            
        except ValueError:
            print("❌ 输入格式错误！请输入两个数字，用空格分隔。")

def main():
    # 初始化游戏
    game = [[' ' for _ in range(3)] for _ in range(3)]  # 3x3游戏棋盘
    current_player = 'X'  # 当前玩家，X先开始
    
    # 游戏欢迎信息
    print("🎮 欢迎来到井字棋游戏！")
    print("📝 游戏规则：")
    print("   • X = 玩家1，O = 玩家2")
    print("   • 轮流在棋盘上标记，先连成三个的获胜")
    print("   • 输入格式：行号 列号 (例如: 1 2)")
    print("=" * 40)
    
    # 显示初始棋盘
    display_board(game)
    
    # 游戏主循环（最多9轮）
    for round_num in range(9):
        # 显示当前玩家
        player_name = "玩家1" if current_player == 'X' else "玩家2"
        print(f"🎯 轮到 {player_name} ({current_player}) 了！")
        
        # 获取有效输入
        i, j = get_valid_input(game)
        
        # 在棋盘上标记
        game[i][j] = current_player
        
        # 显示更新后的棋盘
        display_board(game)
        
        # 检查是否获胜
        if is_win(game):
            print(f"🎉 恭喜！{player_name} ({current_player}) 获胜！")
            break
        
        # 检查是否平局（最后一轮且无人获胜）
        if round_num == 8:
            print("🤝 游戏平局！双方都很厉害！")
            break
        
        # 切换玩家
        current_player = 'O' if current_player == 'X' else 'X'
    
    print("\n🎮 游戏结束，感谢游玩！")

if __name__ == "__main__":
    main()
