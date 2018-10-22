

samples = [
    {'id': 1, 'content': 'This is the first sample'},
    {'id': 2, 'content': 'This is the first sample'}
]

def get_all_samples():
    return samples


def save_new_sample(data):
    if next((s for s in samples if s['id'] == data['id']), None):
        return None
    else:
        samples.append(data)
        return data['id']


def get_a_sample(sample_id):
    return next((s for s in samples if s['id'] == sample_id), None)