import torch

def accuracy(output, target, num=1):
    with torch.no_grad():
        if isinstance(target, (tuple, list)):
            
            _, preds = torch.max(output, dim=1)
            targets1, targets2, lam = target
            correct1 = preds.eq(targets1).sum().item()
            correct2 = preds.eq(targets2).sum().item()
            accuracy = (lam * correct1 + (1 - lam) * correct2) / num
        else :
            pred = torch.argmax(output, dim=1)
            assert pred.shape[0] == len(target)
            correct = 0
            correct += torch.sum(pred == target).item()
            accuracy = correct / len(target)
    return accuracy

def top_k_acc(output, target, k=3):
    with torch.no_grad():
        pred = torch.topk(output, k, dim=1)[1]
        assert pred.shape[0] == len(target)
        correct = 0
        for i in range(k):
            correct += torch.sum(pred[:, i] == target).item()
    return correct / len(target)
