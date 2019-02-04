pubg
==============================

![Project Logo](https://raw.githubusercontent.com/ereidelbach/Images/master/pubgLogo.png)

PUBG Finish Placement Prediction: A Kaggle-based playground code competition ending in January 2019. A large number of anonymized game data is provided from which a model shall be created that predicts players' finishing placement based on their final stats, on a scale from 1 (first place) to 0 (last place).

More information can be found on the official Kaggle competition <a href="https://www.kaggle.com/c/pubg-finish-placement-prediction/data">site</a>.

Data Dictionary
------------

| Variable | Type | Description |
|----------|------|-------------|
| Id | string | Player’s Id |
|groupId | string | ID to identify a group within a match. If the same group of players plays in different matches, they will have a different groupId each time.|
|matchId | string | ID to identify match. There are no matches that are in both the training and testing set.|
|assists | float | Number of enemy players this player damaged that were killed by teammates. |
| boosts | float | Number of boost items used. |
| damageDealt | float | Total damage dealt. Note: Self inflicted damage is subtracted. |
| DBNOs | float | Number of enemy players knocked. |    
| headshotKills | float | Number of enemy players killed with headshots.|
| heals | float | Number of healing items used. |
| killPlace | float | Ranking in match of number of enemy players killed. |
|killPoints | float | Kills-based external ranking of player. (Think of this as an Elo ranking where only kills matter.) If there is a value other than -1 in rankPoints, then any 0 in killPoints should be treated as a “None”.|
| kills | float | Number of enemy players killed.|
|killStreaks | float | Max number of enemy players killed in a short amount of time.|
| longestKill | float | Longest distance between player and player killed at time of death. This may be misleading, as downing a player and driving away may lead to a large longestKill stat.|
| matchDuration | float | Duration of match in seconds. |
| matchType | string | Identifies the game mode that the data comes from. The standard modes are “solo”, “duo”, “squad”, “solo-fpp”, “duo-fpp”, and “squad-fpp”; other modes are from events or custom matches.|
|maxPlace | float | Worst placement we have data for in the match. This may not match with numGroups, as sometimes the data skips over placements.|
|numGroups | float |Number of groups we have data for in the match.|
|rankPoints | float | Elo-like ranking of player. This ranking is inconsistent and is being deprecated in the API’s next version, so use with caution. Value of -1 takes place of “None”.|
|revives | float | Number of times this player revived teammates.
|rideDistance | float | Total distance traveled in vehicles measured in meters.|
|roadKills | float | Number of kills while in a vehicle.|
|swimDistance | float | Total distance traveled by swimming measured in meters.|
|teamKills | float | Number of times this player killed a teammate.
|vehicleDestroys | float | Number of vehicles destroyed.|
|walkDistance | float | Total distance traveled on foot measured in meters.|
|weaponsAcquired | float | Number of weapons picked up.|
|winPoints | float | Win-based external ranking of player. (Think of this as an Elo ranking where only winning matters.) If there is a value other than -1 in rankPoints, then any 0 in winPoints should be treated as a “None”.|
|winPlacePerc | float | **<span style="color:red">The target of prediction.</span>** This is a percentile winning placement, where 1 corresponds to 1st place, and 0 corresponds to last place in the match. It is calculated off of maxPlace, not numGroups, so it is possible to have missing chunks in a match.|

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
