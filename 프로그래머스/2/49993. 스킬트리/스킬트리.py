def solution(skill, skill_trees):
    cnt = 0

    for tree in skill_trees:
        can = True
        first = -1

        if skill[0] in tree:
            first = tree.index(skill[0])
        else:
            first = -1

        for i in range(1, len(skill)):
            c = skill[i]
            if c in tree:
                next_skill = tree.index(c)

                # 이전 스킬(skill[i-1])이 tree에 없는 경우 → 선행 스킬 없이 다음 스킬 배움
                if skill[i-1] not in tree:
                    can = False
                    break

                if first > next_skill:
                    can = False
                    break

                first = next_skill

        if can:
            print(tree)
            cnt += 1

    return cnt
