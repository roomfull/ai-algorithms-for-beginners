"""P058：一次D→G交替更新，G使用新D。"""
import sys
import math


def sigmoid(z):
    if z >= 0:
        return 1/(1+math.exp(-z))
    e = math.exp(z)
    return e/(1+e)


def softplus(z):
    return max(z, 0)+math.log1p(math.exp(-abs(z)))


def solve(raw):
    real, z, a, g, w, b, lr_d, lr_g = map(float, raw.split())
    fake = a*z+g
    real_logit, fake_logit = w*real+b, w*fake+b
    p_real, p_fake = sigmoid(real_logit), sigmoid(fake_logit)
    loss_d = softplus(-real_logit)+softplus(fake_logit)
    dw = (p_real-1)*real+p_fake*fake
    db = p_real-1+p_fake
    new_w, new_b = w-lr_d*dw, b-lr_d*db
    # 判别器更新后重算生成器损失；fake尚未改变。
    new_fake_logit = new_w*fake+new_b
    loss_g = softplus(-new_fake_logit)  # 非饱和生成器目标。
    chain = (sigmoid(new_fake_logit)-1)*new_w
    new_a, new_g = a-lr_g*chain*z, g-lr_g*chain
    return f'{loss_d:.12g} {loss_g:.12g}\n{new_a:.12g} {new_g:.12g} {new_w:.12g} {new_b:.12g}'


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
