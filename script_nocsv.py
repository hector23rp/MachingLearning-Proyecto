import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from scipy.io import loadmat


def create_features(XX, tmin, tmax, sfreq, tmin_original=-0.5):
    """Creation of the feature space:
    - restricting the time window of MEG data to [tmin, tmax]sec.
    - Concatenating the 306 timeseries of each trial in one long
      vector.
    - Normalizing each feature independently (z-scoring).
    """
    print "Applying the desired time window."
    beginning = np.round((tmin - tmin_original) * sfreq).astype(np.int)
    end = np.round((tmax - tmin_original) * sfreq).astype(np.int)
    XX = XX[:, :, beginning:end].copy()

    print "2D Reshaping: concatenating all 306 timeseries."
    XX = XX.reshape(XX.shape[0], XX.shape[1] * XX.shape[2])

    print "Features Normalization."
    XX -= XX.mean(0)
    XX = np.nan_to_num(XX / XX.std(0))

    return XX

if __name__ == '__main__':

    print "DecMeg2014: https://www.kaggle.com/c/decoding-the-human-brain"
    print
    subjects_train = range(13, 16) # use range(1, 17) for all subjects
    print "Training on subjects", subjects_train 

    # We throw away all the MEG data outside the first 0.5sec from when
    # the visual stimulus start:
    tmin = 0.0
    tmax = 0.500
    print "Restricting MEG data to the interval [%s, %s]sec." % (tmin, tmax)

    X_train = []
    y_train = []
    X_test = []
    ids_test = []

    print
    print "Creating the trainset."
    for subject in subjects_train:
        filename = './data/data/train_subject%02d.mat' % subject
        print "Loading", filename
        data = loadmat(filename, squeeze_me=True)
        XX = data['X']
        yy = data['y']
        sfreq = data['sfreq']
        tmin_original = data['tmin']
        print "Dataset summary:"
        print "XX:", XX.shape
        print "yy:", yy.shape
        print "sfreq:", sfreq

        XX = create_features(XX, tmin, tmax, sfreq)

        X_train.append(XX)
        y_train.append(yy)

    X_train = np.vstack(X_train)
    y_train = np.concatenate(y_train)
    print "Trainset:", X_train.shape

    X_train, X_test, y_train, y_test = train_test_split(X_train,y_train,test_size=0.2)

    print(X_train.shape)
    print(X_test.shape)
    print(y_train.shape)
    print(y_test.shape)

    print "Testset:", X_test.shape

    print
    clf = LogisticRegression(random_state=0) # Beware! You need 10Gb RAM to train LogisticRegression on all 16 subjects!
    print "Classifier:"
    print clf
    print "Training."
    clf.fit(X_train, y_train)
    print "Predicting."
    y_pred = clf.predict(X_test)
    print "Accuracy del Clasificador con 80*100 entrenamiento y 20*100 test"
    acc = metrics.accuracy_score(y_test,y_pred)
    print(acc)
    """ print
    filename_submission = "submission.csv"
    print "Creating submission file", filename_submission
    f = open(filename_submission, "w")
    print >> f, "Id,Prediction"
    for i in range(len(y_pred)):
        print >> f, str(ids_test[i]) + "," + str(y_pred[i])

    f.close() """
    print "Done."