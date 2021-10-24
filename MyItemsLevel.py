level_scale = (float(1 + 0.05)) / float(1)
print('Damage calculator - MyItems')
# input module
print('Bây giờ, bạn hãy nhập vào chỉ số của vật phẩm khi mới level 1!')
min_dame = float(input('Nhập sát thương (Tối thiểu): '))
max_dame = float(input('Nhập sát thương (Tối đa): '))
# calculation request
req_level = int(input('Nhập vào level muốn xem: '))
ratio = float(max_dame / min_dame)
addon = (min_dame * level_scale) - min_dame
min_new = float(min_dame + addon*(req_level-1))
max_new = min_new * ratio
print('Khi vật phẩm đạt đến level %d:' % (req_level,))
print('  - Sát thương tối thiểu: %s -> %s' % (round(min_dame, 2), round(min_new, 2)))
print('  - Sát thương tối đa: %s -> %s' % (round(max_dame, 2), round(max_new, 2)))
print('\nXong hết rồi đấy :3')
