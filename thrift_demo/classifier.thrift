typedef list<double> Feature

service Classifier{
    i64 predict(1: Feature feature);
}

