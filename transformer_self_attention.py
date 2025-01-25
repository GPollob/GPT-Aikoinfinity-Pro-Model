import torch
import torch.nn.functional as F

# Example: Simplified Scaled Dot-Product Attention
def scaled_dot_product_attention(query, key, value, mask=None):
    """
    Compute attention scores and apply to value.
    Args:
        query, key, value: Tensors of shape [batch_size, seq_len, d_model]
        mask: Optional mask tensor
    """
    d_k = query.size(-1)
    scores = torch.matmul(query, key.transpose(-2, -1)) / torch.sqrt(torch.tensor(d_k, dtype=torch.float32))
    if mask is not None:
        scores = scores.masked_fill(mask == 0, float('-inf'))
    attention = F.softmax(scores, dim=-1)
    return torch.matmul(attention, value)

# Example input tensors
batch_size, seq_len, d_model = 2, 5, 64
query = torch.rand(batch_size, seq_len, d_model)
key = torch.rand(batch_size, seq_len, d_model)
value = torch.rand(batch_size, seq_len, d_model)

# Compute attention
output = scaled_dot_product_attention(query, key, value)
print("Attention Output:", output.shape)
