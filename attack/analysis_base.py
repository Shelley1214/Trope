

import json, os, re
import pandas as pd

path = "output"
# base
_plot = {
    "Big Bad":['MoonOverMiami', 'StarterFor10', 'Secretariat', 'CantHardlyWait', 'MarleyAndMe', 'Evita', 'WeWereSoldiers', 'TheChristmasToy', 'ShatteredGlass', 'StuckInLove', 'NightMoves', 'TheDevilsArithmetic', 'QuickChange', 'Ararat', 'WhistleDownTheWind', 'FindingNeverland', 'BlackSnakeMoan', 'Poseidon', 'SnowCake', 'BlackSea', 'HeadOfState', 'Twister', 'ItHappenedHere', 'TheIncredibleShrinkingMan', 'TheAmericanPresident', 'W', 'Goodfellas', 'RabbitFire', 'CoolRunnings', 'HeartsInAtlantis'],   
    "Blatant Lies":['CloakAndDagger', 'StarterFor10', 'DeadAndDeader', 'JesusChristVampireHunter', 'CantHardlyWait', 'PoolhallJunkies', 'QuickChange', 'AnAllDogsChristmasCarol', 'Stagecoach', 'TheAdventuresOfPlutoNash', 'TheDevilsArithmetic', 'NancyDrew', 'LakePlacid3', 'MissionImpossibleII', 'MarleyAndMe', 'DeadSpaceDownfall', 'CoolRunnings', 'SmallTimeCrooks', 'Popeye', 'StarTrekTheWrathOfKhan', 'ANightmareOnElmStreet3DreamWarriors', 'WeWereSoldiers', 'SnowCake', 'StarTrekGenerations', 'Anaconda', 'TheIncredibleShrinkingMan', 'Secretariat', 'LittleRuralRidingHood', 'TheAngelsShare', 'AvatarTheLastAirbender'],    "Kick the Dog":['CloakAndDagger', 'MarleyAndMe', 'FuneralInBerlin', 'RabbitFire', 'LakePlacid3', 'Horsemen', 'Ararat', 'CoolRunnings', 'Poseidon', 'Evita', 'NightMoves', 'ScaryMovie', 'ShatteredGlass', 'HeadOfState', 'WeWereSoldiers', 'SnowCake', 'LittleRuralRidingHood', 'WhistleDownTheWind', 'TheAmericanPresident', 'TheIncredibleShrinkingMan', 'W', 'TheChristmasToy', 'DeadSpaceDownfall', 'FromBeyond', 'BartonFink', 'QuickChange', 'FindingNeverland', 'Twister', 'InvasionOfTheBodySnatchers', 'NancyDrew'],
    "Kick the Dog":['CloakAndDagger', 'MarleyAndMe', 'FuneralInBerlin', 'RabbitFire', 'LakePlacid3', 'Horsemen', 'Ararat', 'CoolRunnings', 'Poseidon', 'Evita', 'NightMoves', 'ScaryMovie', 'ShatteredGlass', 'HeadOfState', 'WeWereSoldiers', 'SnowCake', 'LittleRuralRidingHood', 'WhistleDownTheWind', 'TheAmericanPresident', 'TheIncredibleShrinkingMan', 'W', 'TheChristmasToy', 'DeadSpaceDownfall', 'FromBeyond', 'BartonFink', 'QuickChange', 'FindingNeverland', 'Twister', 'InvasionOfTheBodySnatchers', 'NancyDrew']
}

trp = "Big Bad"
# trp = "Kick the Dog"
# trp = "Blatant Lies"
base_output = {}
filename = []
output = []
for file in _plot[trp]:
    file = file + ".txt"

    # attack file
    f = open(f"output/{path}/{file}")
    # origin attack file
    preds = open(f"output/trope_output/base/gpt_4/{file}")

    file_content = f.read()
    file_content = file_content.split("\n")
    pred = []
    for i in range(len(file_content)):
        match = re.search(r"'([^']*)'", file_content[i])
        if match and match.group(1) == trp:
            pred.append(file_content[i])
    filename.append(file.split(".")[0])
    output.append(pred)

base_output = {
    "filename": filename,
    "pred": output
}
df = pd.DataFrame(base_output)
df.to_csv(f"{trp}.csv", index=False)

