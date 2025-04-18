import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.model_selection import train_test_split


"""
Matrix factorization with TorchRec
"""
class MF(nn.Module):
    def __init__(self, num_users, num_items, emb_size=100):
        super(MF, self).__init__()
        self.user_emb = nn.Embedding(num_users, emb_size)
        self.item_emb = nn.Embedding(num_items, emb_size)
        # initializing our matrices with a positive number generally will yield better results
        self.user_emb.weight.data.uniform_(0, 0.5)
        self.item_emb.weight.data.uniform_(0, 0.5)
    def forward(self, u, v):
        u = self.user_emb(u)
        v = self.item_emb(v)

        # taking the dot product
        return (u*v).sum(1)


def train_epocs(model, epochs=10, lr=0.01, wd=0.0):
    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=wd)
    model.train()
    for i in range(epochs):
        usernames = torch.LongTensor(train_df.UserId.values)
        game_titles = torch.LongTensor(train_df.TitleId.values)
        ratings = torch.FloatTensor(train_df.Userscore.values)
        y_hat = model(usernames, game_titles)
        loss = F.mse_loss(y_hat, ratings)
        optimizer.zero_grad()  # reset gradient
        loss.backward()
        optimizer.step()
        print(loss.item())
    test(model)


def test(model):
    model.eval()
    usernames = torch.LongTensor(test_df.UserId.values)
    game_titles = torch.LongTensor(test_df.TitleId.values)
    ratings = torch.FloatTensor(test_df.Userscore.values)
    y_hat = model(usernames, game_titles)
    loss = F.mse_loss(y_hat, ratings)
    print("test loss %.3f " % loss.item())
    return loss, ratings


if __name__ == '__main__':
    num_users, num_items = 100, 100 #6096, 9096
    dataset = pd.read_csv("data/train.csv")
    model = MF(num_users, num_items, emb_size=100)
    train_df, valid_df = train_test_split(dataset, test_size=0.2)
    # resetting indices to avoid indexing errors
    train_df = train_df.reset_index(drop=True)
    test_df = valid_df.reset_index(drop=True)
    train_epocs(model, epochs=10, lr=0.01, wd=0.0)
    test(model)
    torch.save(model.state_dict(), 'model.pt')
    # model.load_state_dict(torch.load('model.pt'))
