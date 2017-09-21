import utils


class NaverWebtoonCrawler:
    def __init__(self, webtoon_id):
        self.webtoon_id = webtoon_id
        self.episode_list = list()
        self.new_episode = []

    def total_episode_count(self):
        """
        webtoon_id에 해당하는 실제 웹툰의 총 episode수를 리턴
        requests를 사용
        :return: 총 episode수 (int)
        """
        self.new_episode = utils.get_webtoon_episode_list(self.webtoon_id)
#         self.new_episode = e
        return int(self.new_episode[0].no)

    def up_to_date(self):
        """
        현재 가지고있는 episode_list가 웹상의 최신 episode까지 가지고 있는지
        :return: boolean값
        """
        if self.episode_list == []:
            return 'self.episode_list 에 아무것도 없음 로드해라'
        if self.total_episode_count() == int(self.episode_list[0].no):
            return True
        else:
            return False

    def update_episode_list(self, force_update=False):
        """
        self.episode_list에 존재하지 않는 episode들을 self.episode_list에 추가
        :param force_update: 이미 존재하는 episode도 강제로 업데이트
        :return: 추가된 episode의 수 (int)
        """
        new_list = []
        for i in range(0, 1000):
            page = utils.get_webtoon_episode_list(self.webtoon_id, i)
            new_list.extend(page)
            # page = [ep1, ep2, ep3...]
            if int(page[-1].no) == 1:
                break
                

        if self.episode_list == []:
            return '로드부터 하세요'
        
        # 같으면 안함
        if len(new_list) == len(self.episode_list):
            return '최신리스트와 똑같음'
        else:
            diff = list(set(new_list) - set(self.episode_list))
            if force_update:
                self.episode_list = new_list
                return len(new_list)
            else:
                self.episode_list = self.episode_list + diff
                self.episode_list = sorted(self.episode_list, reverse=True, key=lambda x: int(x.no))
                return len(diff)
        
    def save(self, path=None):
        """
        현재폴더를 기준으로 db/<webtoon_id>.txt 파일에
        pickle로 self.episode_list를 저장
        :return: 성공여부
        """
        file_name = '{}.txt'.format(self.webtoon_id)
        path = '/'.join(path+file_name)  if path else file_name
        
        with open(file_name, 'wb') as p:
            pickle.dump(self.new_episode, p)

    def load(self, path=None):
        """
        현재폴더를 기준으로 db/<webtoon_id>.txt 파일의 내용을 불러와
        pickle로 self.episode_list를 복원
        :return:
        """
        with open('{}.txt'.format(self.webtoon_id), 'rb') as p:
            self.episode_list = pickle.load(p)
        return self.episode_list

nwc = NaverWebtoonCrawler(651673)
print(nwc.total_episode_count)