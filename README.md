"# sr2022" 

<!-- 再作成 -->
conda remove -n sr_2022 --all
conda create -n sr_2022 python=3.7
activate sr_2022
conda install jupyter notebook
conda install pandas
pip install -U ginza ja_ginza

<!-- Python　Ginzaのインストールはcondaコマンドの後 -->
pip install -U ginza https://github.com/megagonlabs/ginza/releases/download/latest/ja_ginza_electra-latest-with-model.tar.gz

<!-- 仮想環境一覧 -->
conda info -e

conda list