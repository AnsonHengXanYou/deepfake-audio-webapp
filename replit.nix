{ pkgs }: {
  deps = [
    pkgs.python310Full
    pkgs.python310Packages.pip
    pkgs.python310Packages.setuptools
    pkgs.python310Packages.wheel
    pkgs.python310Packages.flask
    pkgs.python310Packages.numpy
    pkgs.python310Packages.librosa
    pkgs.python310Packages.scikit-learn
    pkgs.python310Packages.joblib
  ];
}
