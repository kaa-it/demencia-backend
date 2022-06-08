import datetime

import graphene
from django.core.validators import validate_email
from graphene_django import DjangoObjectType
from graphene_file_upload.scalars import Upload

from django.core.exceptions import ValidationError

from .models import Answer, DementiaTestCase


now = datetime.datetime.now()
ALLOWED_FILES_TYPE = ["jpg", "jpeg", "img", "png"]


class DementiaTestCaseType(DjangoObjectType):
    id = graphene.ID(description="ID теста")

    class Meta:
        model = DementiaTestCase
        fields = ("id",)


class AnswerType(DjangoObjectType):
    id = graphene.ID(description="ID ответа")
    answer_value = graphene.String(description="Значение ответа")
    question = graphene.Int(description="Номер вопроса")
    image = graphene.String(description="Изображение")
    test_case = graphene.Field(DementiaTestCaseType, description="Экземпляр теста")

    class Meta:
        model = Answer
        fields = ("id", "answer_value", "test_case", "question", "image")


class DementiaTestCaseInput(graphene.InputObjectType):
    id = graphene.ID(description="ID теста", required=True)


class AnswerInput(graphene.InputObjectType):
    image = Upload(description="Изображение")
    answer_value = graphene.String(description="Значение ответа")
    test_case = graphene.InputField(DementiaTestCaseInput, description="Экземпляр теста", required=True)
    question = graphene.Int(description="Номер вопроса", required=True)


class CreateAnswer(graphene.Mutation):
    answer = graphene.Field(AnswerType)
    ok = graphene.Boolean()

    class Arguments:
        input = AnswerInput(required=True)

    def mutate(self, info, input=None):  # noqa
        answer_value = input.answer_value or Answer._meta.get_field("answer_value").get_default()
        test_case = DementiaTestCase.objects.get(id=input.test_case.id)
        question = input.question

        if question == 1:
            if not answer_value:
                raise ValidationError("Поле не может быть пустым")

        if question in [1, 8, 17, 22, 25]:
            escape = {"'", '"', "`", "{", "}", "[", "]", "<", ">", "/", "\\", "!", "="}
            if answer_value:
                tmp = set(answer_value)
                if tmp.intersection(escape):
                    raise ValidationError("Недопустимые символы в строке")

        if question == 2 or question == 14:
            try:
                datetime.datetime.strptime(answer_value, "%d-%m-%Y")
            except ValueError:
                raise ValueError("Некорректный формат даты, пример даты: 20-12-2022")

        if question == 4:
            try:
                validate_email(answer_value)
            except ValidationError:
                raise ValueError("Некорректный формат email")

        if question == 15 or question == 16:
            alphabet = {
                "а",
                "б",
                "в",
                "г",
                "д",
                "е",
                "ё",
                "ж",
                "з",
                "и",
                "й",
                "к",
                "л",
                "м",
                "н",
                "о",
                "п",
                "р",
                "с",
                "т",
                "у",
                "ф",
                "х",
                "ц",
                "ч",
                "ш",
                "щ",
                "ъ",
                "ы",
                "ь",
                "э",
                "ю",
                "я",
            }
            tmp = set(answer_value.lower())
            for i in tmp:
                if i.isalpha() and i not in alphabet:
                    raise ValidationError("Недопустимые символы в строке")

        if question == 15:
            escape = {"'", '"', "`", "{", "}", "[", "]", "<", ">", "/", "\\", "!", "=", "_", ".", ","}
            if answer_value.intersection(escape):
                raise ValidationError("Недопустимые символы в строке")

        if question == 16:
            escape = {"'", '"', "`", "{", "}", "[", "]", "<", ">", "/", "\\", "!", "=", "_", "."}
            if answer_value.intersection(escape) or answer_value.count(",") > 1:
                raise ValidationError("Недопустимые символы в строке")

        if question == 18:
            try:
                _ = float(answer_value.replace(",", "."))
            except Exception:
                raise ValidationError("Недопустимое значение")

        image = input.image or Answer._meta.get_field("image").get_default()
        if question < 1 or question > 25:
            raise ValidationError("Номер вопроса не может быть меньше 1 и больше 25.")

        if not (question in [20, 21]) and image:
            raise ValidationError(f"Вопрос {question} должен содержать только ответ и не может включать изображение")

        if question in [20, 21] and answer_value:
            raise ValidationError(f"Вопрос {question} должен содержать только изображение и не может включать ответ")

        if question in [20, 21] and not (image):
            raise ValidationError(f"Вопрос {question} должен содержать изображение")

        file_name = str(image)
        if question in [20, 21]:
            if ("." not in file_name) or (str(image).split(".")[-1].lower() not in ALLOWED_FILES_TYPE):
                raise ValidationError(
                    f"Для загрузки разрешены только следующие типы файлов: {', '.join(ALLOWED_FILES_TYPE)}"
                )

        instance, _ = Answer.objects.update_or_create(
            test_case=test_case, question=question, defaults={"answer_value": answer_value, "image": image}
        )

        ok = True
        return CreateAnswer(answer=instance, ok=ok)


class Mutation(graphene.ObjectType):
    create_answer = CreateAnswer.Field()


schema = graphene.Schema(mutation=Mutation)
