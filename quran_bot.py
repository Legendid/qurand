import nextcord
from nextcord.ext import commands
import fitz
import os
intents = nextcord.Intents().all()

class BotSync(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="", intents=intents)

bot = BotSync()



class QuranCommand:
  def __init__(self, interaction):
      self.interaction = interaction
      self.page_number = 3

  async def generate_pdf_page(self, page_number):
      f = open("big-quran_compressed.pdf")
      pdf_document = fitz.open(f)
      page = pdf_document.load_page(page_number - 1)
      pix = page.get_pixmap()
      image_path = f'page_{page_number}.png'
      pix.save(image_path)
      f.close()
      pdf_document.close()
      return image_path

  async def edit_pdf_page(self, page_number):
        image_path = await self.generate_pdf_page(page_number)
        await self.interaction.edit(
            file=nextcord.File(image_path),
            view=quran1(page_number, self.interaction.user.id)
        )
        os.remove(image_path)

  async def send_pdf_page(self):
      image_path = await self.generate_pdf_page(self.page_number)
      await self.interaction.send(
          file=nextcord.File(image_path),
          view=quran1(self.page_number, self.interaction.user.id)
          , ephemeral=True
      )
      os.remove(image_path)

class send_quran1(nextcord.ui.View):
    def __init__(self):
        super().__init__()

    @nextcord.ui.button(label="احصل على المصحف")
    async def whhh(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        command_q = QuranCommand(interaction)
        quran_view = quran1(command_q.page_number, interaction.user.id)

        await command_q.send_pdf_page()
        await interaction.send(
            file=nextcord.File(quran_view.image_path),
            view=quran_view
            , ephemeral=True
        )
      
   
        
class quran1(nextcord.ui.View):
          def __init__(self, page_number, user_id):
            super().__init__()
            self.page_number = page_number
            self.user_id = user_id
          
        
          @nextcord.ui.select(placeholder="اختر السورة", options=[
              nextcord.SelectOption(label="الفاتحه", value="4"),
              nextcord.SelectOption(label="البقرة", value="5"),
              nextcord.SelectOption(label="آل عمران", value="53"),
              nextcord.SelectOption(label="النساء", value="80"),
              nextcord.SelectOption(label="المائدة", value="109"),
              nextcord.SelectOption(label="الأنعام", value="131"),
              nextcord.SelectOption(label="الأعراف", value="154"),
              nextcord.SelectOption(label="الأنفال", value="180"),
              nextcord.SelectOption(label="التوبة", value="190"),
              nextcord.SelectOption(label="يونس", value="211"),

              nextcord.SelectOption(label="هود", value="224"),
              nextcord.SelectOption(label="يوسف", value="238"),
              nextcord.SelectOption(label="الرعد", value="252"),
              nextcord.SelectOption(label="إبراهيم", value="258"),
              nextcord.SelectOption(label="الحجر", value="265"),
              nextcord.SelectOption(label="النحل", value="270"),
              nextcord.SelectOption(label="الإسراء", value="285"),
              nextcord.SelectOption(label="الكهف", value="296"),
              nextcord.SelectOption(label="مريم", value="308"),
              nextcord.SelectOption(label="طه", value="315"),
              nextcord.SelectOption(label="الأنبياء", value="325"),
              nextcord.SelectOption(label="الحج", value="335"),
              nextcord.SelectOption(label="المؤمنون", value="345"),
              nextcord.SelectOption(label="النور", value="353"),
              nextcord.SelectOption(label="الفرقان", value="362"),
              



          ])
          async def cal18181yyl1back(self, select: nextcord.ui.Select, interaction: nextcord.Interaction):
              
            qc = QuranCommand(interaction)
            selected_value = select.values[0]
            self.page_number = int(selected_value)
            await qc.edit_pdf_page(self.page_number)

            if selected_value == "1":
              image_path = await qc.generate_pdf_page(self.page_number)
              file = nextcord.File(image_path)
              await interaction.edit(files=[file], attachments=[], view=self)
              os.remove(image_path)

              self.page_number = int(select.values[0])
              await qc.edit_pdf_page()
              if select.values[0] == "2":
                  image_path = await qc.edit_pdf_page()
                  file = nextcord.File(image_path)
                  await interaction.edit(files=[file], attachments=[], view = self)
                  os.remove(image_path)

              self.page_number = int(select.values[0])
              await qc.edit_pdf_page()
              if select.values[0] == "45":
                  image_path = await edit_pdf_page(interaction, self.page_number)
                  file = nextcord.File(image_path)
                  await interaction.edit(files=[file], attachments=[], view = self)
                  os.remove(image_path)

              self.page_number = int(select.values[0])
              await edit_pdf_page(interaction, self.page_number)
              if select.values[0] == "69":
                  image_path = await edit_pdf_page(interaction, self.page_number)
                  file = nextcord.File(image_path)
                  await interaction.edit(files=[file], attachments=[], view = self)
                  os.remove(image_path)

              self.page_number = int(select.values[0])
              await edit_pdf_page(interaction, self.page_number)
              if select.values[0] == "105":
                    image_path = await edit_pdf_page(interaction, self.page_number)
                    file = nextcord.File(image_path)
                    await interaction.edit(files=[file], attachments=[], view = self)
                    os.remove(image_path)

              self.page_number = int(select.values[0])
              await edit_pdf_page(interaction, self.page_number)
              if select.values[0] == "1":
                  image_path = await edit_pdf_page(interaction, self.page_number)
                  file = nextcord.File(image_path)
                  await interaction.edit(files=[file], attachments=[], view = self)
                  os.remove(image_path)

              if select.values[0] == "136":
                image_path = await qc.generate_pdf_page(136)
                file = nextcord.File(image_path)
                await interaction.edit(file=file)
                os.remove(image_path)

              if select.values[0] == "160":
                image_path = await qc.generate_pdf_page(160)
                file = nextcord.File(image_path)
                await interaction.edit(file=file)
                os.remove(image_path)


                
        
          @nextcord.ui.select(placeholder="اختر سورة", options=[
            nextcord.SelectOption(label="الشعراء", value="370"),
            nextcord.SelectOption(label="النمل", value="380"),
            nextcord.SelectOption(label="القصص", value="388"),
            nextcord.SelectOption(label="العنكبوت", value="399"),
            nextcord.SelectOption(label="الروم", value="407"),
            nextcord.SelectOption(label="لقمان", value="414"),
            nextcord.SelectOption(label="السجدة", value="418"),
            nextcord.SelectOption(label="الاحزاب", value="421"),
            nextcord.SelectOption(label="سبأ", value="431"),
            nextcord.SelectOption(label="فاطر", value="437"),
            nextcord.SelectOption(label="يس", value="443"),
            nextcord.SelectOption(label="الصافات", value="449"),
            nextcord.SelectOption(label="ص" , value="456"),
            nextcord.SelectOption(label="الزمر", value="461"),
            nextcord.SelectOption(label="غافر", value="470"),
            nextcord.SelectOption(label="فصلت", value="480"),
            nextcord.SelectOption(label="الشورى", value="486"),
            nextcord.SelectOption(label="الزخرف", value="492"),
            nextcord.SelectOption(label="الدخان", value="499"),
            nextcord.SelectOption(label="الجاثية", value="502"),
            nextcord.SelectOption(label="الأحقاف", value="505"),
            nextcord.SelectOption(label="محمد", value="510"),
            nextcord.SelectOption(label="الفتح", value="514"),
            nextcord.SelectOption(label="الحجرات", value="518"),
            nextcord.SelectOption(label="ق", value="521"),
            
            
            
       
            

          ])
          async def cal18181yyl1ba111ck(self, select: nextcord.ui.Select, interaction: nextcord.Interaction):
              qc = QuranCommand(interaction)
              selected_value = select.values[0]
              self.page_number = int(selected_value)
              await qc.edit_pdf_page(self.page_number)

              if selected_value == "1":
                  image_path = await qc.generate_pdf_page(self.page_number)
                  file = nextcord.File(image_path)
                  await interaction.edit(files=[file], attachments=[], view=self)
                  os.remove(image_path)

              self.page_number = int(select.values[0])
              await edit_pdf_page(interaction, self.page_number)
              if select.values[0] == "2":
                  image_path = await edit_pdf_page(interaction, self.page_number)
                  file = nextcord.File(image_path)
                  await interaction.edit(files=[file], attachments=[], view = self)
                  os.remove(image_path)

              self.page_number = int(select.values[0])
              await edit_pdf_page(interaction, self.page_number)
              if select.values[0] == "45":
                  image_path = await edit_pdf_page(interaction, self.page_number)
                  file = nextcord.File(image_path)
                  await interaction.edit(files=[file], attachments=[], view = self)
                  os.remove(image_path)

              self.page_number = int(select.values[0])
              await edit_pdf_page(interaction, self.page_number)
              if select.values[0] == "69":
                  image_path = await edit_pdf_page(interaction, self.page_number)
                  file = nextcord.File(image_path)
                  await interaction.edit(files=[file], attachments=[], view = self)
                  os.remove(image_path)

              self.page_number = int(select.values[0])
              await edit_pdf_page(interaction, self.page_number)
              if select.values[0] == "105":
                    image_path = await edit_pdf_page(interaction, self.page_number)
                    file = nextcord.File(image_path)
                    await interaction.edit(files=[file], attachments=[], view = self)
                    os.remove(image_path)

              self.page_number = int(select.values[0])
              await edit_pdf_page(interaction, self.page_number)
              if select.values[0] == "1":
                  image_path = await edit_pdf_page(interaction, self.page_number)
                  file = nextcord.File(image_path)
                  await interaction.edit(files=[file], attachments=[], view = self)
                  os.remove(image_path)

              if select.values[0] == "136":
                image_path = await generate_pdf_page(136)
                file = nextcord.File(image_path)
                await interaction.edit(file=file)
                os.remove(image_path)

              if select.values[0] == "160":
                image_path = await generate_pdf_page(160)
                file = nextcord.File(image_path)
                await interaction.edit(file=file)
                os.remove(image_path)


          @nextcord.ui.select(placeholder="اختر السورة", options=[
                nextcord.SelectOption(label="الذاريات", value="523"),
                nextcord.SelectOption(label="الطور", value="526"),

                nextcord.SelectOption(label="النجم", value = "529"),
                nextcord.SelectOption(label="القمر", value = "531"),

                nextcord.SelectOption(label="الرحمن", value = "534"),
                nextcord.SelectOption(label="الواقعة", value = "537"),
                nextcord.SelectOption(label="الحديد", value = "540"),
                nextcord.SelectOption(label="المجادلة", value = "545"),
                nextcord.SelectOption(label="الحشر", value = "548"),
                nextcord.SelectOption(label="الممتحنة", value = "552"),
                nextcord.SelectOption(label="الصّف", value = "554"),
                nextcord.SelectOption(label="الجمعة", value = "556"),
                nextcord.SelectOption(label="المنافقون", value = "557"),
                nextcord.SelectOption(label="التغابن", value = "559"),
                nextcord.SelectOption(label="الطلاق", value = "561"),
                nextcord.SelectOption(label="التحريم", value = "563"),
                nextcord.SelectOption(label="الملك", value = "565"),
                nextcord.SelectOption(label="القلم", value = "567"),
                nextcord.SelectOption(label="الحاقة", value = "569"),
                nextcord.SelectOption(label="المعراج", value = "571"),
                nextcord.SelectOption(label="نوح", value = "573"),
                nextcord.SelectOption(label="الجن", value = "575"),
                nextcord.SelectOption(label="المزمل", value = "577"),
                nextcord.SelectOption(label="المدثر", value = "578"),
                






          ])
          async def calyy1lback(self, select: nextcord.ui.Select, interaction: nextcord.Interaction):
            qc = QuranCommand(interaction)
            selected_value = select.values[0]
            self.page_number = int(selected_value)
            await qc.edit_pdf_page(self.page_number)

            if selected_value == "1":
                image_path = await qc.generate_pdf_page(self.page_number)
                file = nextcord.File(image_path)
                await interaction.edit(files=[file], attachments=[], view=self)
                os.remove(image_path)

                self.page_number = int(select.values[0])
                await edit_pdf_page(interaction, self.page_number)
                if select.values[0] == "2":
                    image_path = await edit_pdf_page(interaction, self.page_number)
                    file = nextcord.File(image_path)
                    await interaction.edit(files=[file], attachments=[], view = self)
                    os.remove(image_path)

                self.page_number = int(select.values[0])
                await edit_pdf_page(interaction, self.page_number)
                if select.values[0] == "45":
                    image_path = await edit_pdf_page(interaction, self.page_number)
                    file = nextcord.File(image_path)
                    await interaction.edit(files=[file], attachments=[], view = self)
                    os.remove(image_path)

                self.page_number = int(select.values[0])
                await edit_pdf_page(interaction, self.page_number)
                if select.values[0] == "69":
                    image_path = await edit_pdf_page(interaction, self.page_number)
                    file = nextcord.File(image_path)
                    await interaction.edit(files=[file], attachments=[], view = self)
                    os.remove(image_path)

                self.page_number = int(select.values[0])
                await edit_pdf_page(interaction, self.page_number)
                if select.values[0] == "105":
                      image_path = await edit_pdf_page(interaction, self.page_number)
                      file = nextcord.File(image_path)
                      await interaction.edit(files=[file], attachments=[], view = self)
                      os.remove(image_path)

                self.page_number = int(select.values[0])
                await edit_pdf_page(interaction, self.page_number)
                if select.values[0] == "1":
                    image_path = await edit_pdf_page(interaction, self.page_number)
                    file = nextcord.File(image_path)
                    await interaction.edit(files=[file], attachments=[], view = self)
                    os.remove(image_path)

                if select.values[0] == "136":
                  image_path = await generate_pdf_page(136)
                  file = nextcord.File(image_path)
                  await interaction.edit(file=file)
                  os.remove(image_path)

                if select.values[0] == "160":
                  image_path = await generate_pdf_page(160)
                  file = nextcord.File(image_path)
                  await interaction.edit(file=file)
                  os.remove(image_path)
          @nextcord.ui.select(placeholder="اختر سورة", options=[
              nextcord.SelectOption(label="القيامة", value = "580"),
              nextcord.SelectOption(label="الإنسان", value = "581"),
              nextcord.SelectOption(label="المرسلات", value = "583"),
              nextcord.SelectOption(label="النبأ", value = "585"),
              nextcord.SelectOption(label="النازعات", value = "586"),
              nextcord.SelectOption(label="عبس", value = "588"),
              nextcord.SelectOption(label="التكوير", value = "589"),
              nextcord.SelectOption(label="الانفطار والمطففين", value = "590"),
              nextcord.SelectOption(label="الانشقاق", value = "592"),
              nextcord.SelectOption(label="البروج", value = "593"),
              nextcord.SelectOption(label="الطارق والأعلى", value = "594"),
              nextcord.SelectOption(label="الغاشية", value = "595"),
              nextcord.SelectOption(label="الفجر", value = "596"),
              nextcord.SelectOption(label="البلد", value = "597"),
              nextcord.SelectOption(label="الليل والشمس", value = "598"),
              nextcord.SelectOption(label="الضحى والشرح", value = "599"),
              nextcord.SelectOption(label="التين والعلق", value = "600"),
              nextcord.SelectOption(label="القدر والبينة", value = "601"),
              nextcord.SelectOption(label="الزلزلة و العاديات", value = "602"),
              nextcord.SelectOption(label="القارعة والتكاثر", value = "603"),
              nextcord.SelectOption(label="العصر والهمزة والفيل", value = "604"),
              nextcord.SelectOption(label="قريش والماعون والكوثر", value = "605"),
              nextcord.SelectOption(label="الكافرون والنصر والمسد", value = "606"),
            nextcord.SelectOption(label="الإخلاص والفلق والناس", value = "607"),
          ])
          async def ns182828hshs(self , select: nextcord.ui.Select, interaction: nextcord.Interaction):
            qc = QuranCommand(interaction)
            selected_value = select.values[0]
            self.page_number = int(selected_value)
            await qc.edit_pdf_page(self.page_number)

            if selected_value == "1":
              image_path = await qc.generate_pdf_page(self.page_number)
              file = nextcord.File(image_path)
              await interaction.edit(files=[file], attachments=[], view=self)
              os.remove(image_path)

            if select.values[0] == "2":
                  image_path = await edit_pdf_page(interaction, self.page_number)
                  file = nextcord.File(image_path)
                  await interaction.edit(files=[file], attachments=[], view = self)
                  os.remove(image_path)

                  self.page_number = int(select.values[0])
                  await edit_pdf_page(interaction, self.page_number)
            if select.values[0] == "45":
                  image_path = await edit_pdf_page(interaction, self.page_number)
                  file = nextcord.File(image_path)
                  await interaction.edit(files=[file], attachments=[], view = self)
                  os.remove(image_path)

                  self.page_number = int(select.values[0])
                  await edit_pdf_page(interaction, self.page_number)
            if select.values[0] == "69":
                  image_path = await edit_pdf_page(interaction, self.page_number)
                  file = nextcord.File(image_path)
                  await interaction.edit(files=[file], attachments=[], view = self)
                  os.remove(image_path)

                  self.page_number = int(select.values[0])
                  await edit_pdf_page(interaction, self.page_number)
            if select.values[0] == "105":
                    image_path = await edit_pdf_page(interaction, self.page_number)
                    file = nextcord.File(image_path)
                    await interaction.edit(files=[file], attachments=[], view = self)
                    os.remove(image_path)

                    self.page_number = int(select.values[0])
                    await edit_pdf_page(interaction, self.page_number)
            if select.values[0] == "1":
                  image_path = await edit_pdf_page(interaction, self.page_number)
                  file = nextcord.File(image_path)
                  await interaction.edit(files=[file], attachments=[], view = self)
                  os.remove(image_path)

            if select.values[0] == "136":
                image_path = await generate_pdf_page(136)
                file = nextcord.File(image_path)
                await interaction.edit(file=file)
                os.remove(image_path)

            if select.values[0] == "160":
                image_path = await generate_pdf_page(160)
                file = nextcord.File(image_path)
                await interaction.edit(file=file)
                os.remove(image_path)


          @nextcord.ui.button(label='رجوع', style=nextcord.ButtonStyle.grey, custom_id='previous_page')
          async def previous_page(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
            qc = QuranCommand(interaction)
            if self.page_number > 1:
                self.page_number -= 1
                image_path = await qc.generate_pdf_page(self.page_number)
                file = nextcord.File(image_path)
                await interaction.response.edit_message(files=[file], attachments=[], view=self)
                os.remove(image_path)
                await qc.edit_pdf_page(interaction, self.page_number)

          @nextcord.ui.button(label='الخروج', style=nextcord.ButtonStyle.danger, custom_id='exit')
          async def exit(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
                qc = QuranCommand(interaction)
                for item in self.children:
                  item.disabled = True
                  await interaction.message.edit(view=self)# جيت

          @nextcord.ui.button(label='التالي', style=nextcord.ButtonStyle.grey, custom_id='next_page')
          async def next_page(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
            qc = QuranCommand(interaction)
            if self.page_number < 579:
                self.page_number += 1
                image_path = await qc.generate_pdf_page(self.page_number)
                await interaction.edit(files=[nextcord.File(image_path)])
                os.remove(image_path)

            await QuranCommand.send_pdf_page(interaction, page_number)
          

@bot.slash_command(name = "quran")
async def qhhwhw(interaction: nextcord.Interaction):
  await interaction.send("تم", ephemeral=True)
  embed=nextcord.Embed(title="القرآن الكريم لسيرفر عبد الله جميل", description="""**:بسم الله والصلاة والسلام على رسول الله وعلى آله وصحبه أجمعين، أما بعد
                       
                       فهذا مصحف تم إنشاؤه من قبل المطورين بهدف تبادل وكسب الأجر وعدم إهمال قراءة القرآن الكريم، تجدون أدناه 4 قوائم للسور تحتوي على سور القرآن الكريم __( اضغط على السورة المراد قراءتها )__ ، كما توجد أيضاً أزرار للتنقل بين الصفحات بكل سهولة.** """, color=5763719)
  await interaction.send(embed=embed, view=send_quran1())

bot.run("MTE4Nzc1NzE5NTA5ODU5NTM5OA.GKYrTy.Q_6dEvZaNnMJn82CI2Q1-GxuJT0VdfLeiw4n8s")