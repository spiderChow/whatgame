def similar(raw_sentence):
    from sklearn.feature_extraction.text import TfidfVectorizer
    import numpy as np
    from .. import db
    from ..models import User, Sentence



    # get sens to compare from the text file
    sens = []
    with open("V9_generated_question_intent_5000.txt") as f:
        for idx, line in enumerate(f):
            if idx % 3 == 1:
                sens.append(line)

    # read sentences from databases;
    db_sens = Sentence.query.all()
    for s in db_sens:
        sens.append(s.content)


    #get the tf-idf array from sens
    vectorizer = TfidfVectorizer()
    X_train = vectorizer.fit_transform(sens)  # shape is nums x dims

    #transfer input sentence into vector
    input_sent = vectorizer.transform([raw_sentence])
    # cosine and convert into ndarray
    sim_array = (X_train * input_sent.T).A
    # get the most similar sen id and the sen
    idx = np.argmax(sim_array)
    sim_sentence = sens[idx]
    # print(sim_sent)
    return sim_sentence, sim_array.item(idx)