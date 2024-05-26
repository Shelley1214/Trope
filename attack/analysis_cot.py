

import os, json

_plot = {
    "Big Bad":['MoonOverMiami', 'StarterFor10', 'Secretariat', 'CantHardlyWait', 'MarleyAndMe', 'Evita', 'WeWereSoldiers', 'TheChristmasToy', 'ShatteredGlass', 'StuckInLove', 'NightMoves', 'TheDevilsArithmetic', 'QuickChange', 'Ararat', 'WhistleDownTheWind', 'FindingNeverland', 'BlackSnakeMoan', 'Poseidon', 'SnowCake', 'BlackSea', 'HeadOfState', 'Twister', 'ItHappenedHere', 'TheIncredibleShrinkingMan', 'TheAmericanPresident', 'W', 'Goodfellas', 'RabbitFire', 'CoolRunnings', 'HeartsInAtlantis'],   
    "Blatant Lies":[ 'CantHardlyWait' ,'TheShallows', 'FatalAttraction', 'JesusChristVampireHunter', 'AnAllDogsChristmasCarol', 'HigherLearning', 'CloakAndDagger', 'WhistleDownTheWind', 'TheAngelsShare', 'BartonFink', 'DeadAndDeader', 'NightMoves', 'QuickChange', 'BlackSnakeMoan', 'FromBeyond', 'Sleepwalkers', 'TheAdventuresOfPlutoNash', 'StreetsOfFire', 'FindingNeverland', 'TheTenCommandments', 'CoolRunnings', 'Evita', 'WeWereSoldiers', 'MissionImpossibleII', 'Poseidon', 'Goodfellas', 'NancyDrew', 'InvasionOfTheBodySnatchers', 'SnowCake', 'TheIncredibleShrinkingMan'],
    "Kick the Dog": ['CloakAndDagger', 'MarleyAndMe', 'FuneralInBerlin', 'RabbitFire', 'LakePlacid3', 'Horsemen', 'Ararat', 'CoolRunnings', 'Poseidon', 'Evita', 'NightMoves', 'ScaryMovie', 'ShatteredGlass', 'HeadOfState', 'WeWereSoldiers', 'SnowCake', 'LittleRuralRidingHood', 'WhistleDownTheWind', 'TheAmericanPresident', 'TheIncredibleShrinkingMan', 'W', 'TheChristmasToy', 'DeadSpaceDownfall', 'FromBeyond', 'BartonFink', 'QuickChange', 'FindingNeverland', 'Twister', 'InvasionOfTheBodySnatchers', 'NancyDrew']
}

print(len(_plot["Blatant Lies"]))
gt = json.load(open("../subset.json"))
cnt  = 0
for k,v in gt.items():
    if k not in _plot["Big Bad"]:
        continue
    preds = json.load(open(f"output/binary_gpt4_cot/{k}.json"))
    for pred in preds:
        if pred["Trope"] == "Big Bad" and pred["Answer"] != 'yes':
            cnt += 1

cnt = 0
_cnt = 0
trp = "Big Bad"
# trp = "Blatant Lies"
for k in _plot[trp]:
    if not os.path.exists(f"tmp/{k}.json"):
        print(k)
        continue
    _cnt += 1
    datas= json.load(open(f"tmp/{k}.json"))
    for data in datas:
        if data["Trope"] != trp:
            continue
        else:
            if data["Answer"] != 'yes':
                continue
            if type(data['Thought']) == list:
                related_para = data['Thought'][0]['Relevant Paragraphs']
                attack_para = data['Attack_Paragraphs']
                if attack_para in related_para or related_para.lower() == "all":
                    cnt += 1
                else:
                    print(k)
                    print("related", related_para)
                    print("attack",attack_para)
                    print("----------------")

print("success", cnt)
print("total", _cnt)
print(round(cnt*100/_cnt, 2))