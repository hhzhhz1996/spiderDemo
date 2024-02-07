import requests
from bs4 import BeautifulSoup
import os

# 替换为要爬取的网页URL
home_url = ("https://www.bigbigwork.com/wh/w1.html?t=dz&utm_source=baidu&utm_medium=sem"
            "&utm_campaign=%28免%29-Gratisography&utm_content=核心词"
            "&utm_term=gratisography&bd_vid=8667216400394607439")
# 图片保存路径
dir_path = os.path.expanduser('~/Desktop/img/')


def save_path_check(dir_path: str):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def get_img_url(url: str):
    try:
        # 发送HTTP请求
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        response.encoding = response.apparent_encoding  # 设置响应编码

        # 解析网页内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 提取标题
        title = soup.title.string if soup.title else "No Title"

        # 提取链接
        return [a['src'] for a in soup.find_all('img')]

    except requests.RequestException as e:
        print("Error:", str(e))


def download_image(url, save_path: str):
    try:
        # 发送GET请求获取图片内容
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 确保请求成功

        # 打开文件以二进制写入模式
        with open(save_path, 'wb') as file:
            # 将图片内容写入文件
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Image downloaded and saved to {save_path}")

    except requests.RequestException as e:
        print(f"Error downloading the image: {str(e)}")


def url_format(url: str):
    return 'https:' + url if url.startswith('//') else url


def get_suffix(url: str):
    if url.endswith('jpg'):
        return '.jpg'
    elif url.endswith('png'):
        return '.png'
    elif url.endswith('svg'):
        return '.svg'
    else:
        return ''


if __name__ == "__main__":

    # 路径检查
    save_path_check(dir_path)

    links = get_img_url(home_url)
    count = 1
    for idx, link in enumerate(links):
        suffix = get_suffix(link)
        if suffix != '.jpg':
            continue
        file_name = str(count) + suffix
        count += 1
        download_image(url_format(link), os.path.join(dir_path, file_name))
