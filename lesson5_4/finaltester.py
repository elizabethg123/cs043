#[INSERT CODE HERE. If the answer is right, show the “correct” message.
  #  If it’s wrong, show the “wrong” message.]

if (f1*f2==params['answer'][0]):
    page +='''
    <h2 style="background-color:green">Correct, {}x{}={}</h2>
    '''.format(f1,f2,answer1)
else:
    page += '''
        <h2 style="background-color:red">Wrong, {}x{}&#8800;{}</h2>
        '''.format(f1, f2, answer1)


