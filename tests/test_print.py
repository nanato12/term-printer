import pytest
from pytest import CaptureFixture

from term_printer import Color, StdText, cprint
from term_printer.consts.format import Format


class TestPrint:
    def test_default(self, capfd: CaptureFixture) -> None:
        cprint(StdText("no option"))
        out, err = capfd.readouterr()
        assert out == "no option\n"
        assert err == ""

    @pytest.mark.parametrize(
        "stdout, expected",
        [
            (StdText("black", Color.BLACK), "\033[30mblack\033[m\n"),
            (StdText("red", Color.RED), "\033[31mred\033[m\n"),
            (StdText("green", Color.GREEN), "\033[32mgreen\033[m\n"),
            (StdText("yellow", Color.YELLOW), "\033[33myellow\033[m\n"),
            (StdText("blue", Color.BLUE), "\033[34mblue\033[m\n"),
            (StdText("magenta", Color.MAGENTA), "\033[35mmagenta\033[m\n"),
            (StdText("cyan", Color.CYAN), "\033[36mcyan\033[m\n"),
            (StdText("white", Color.WHITE), "\033[37mwhite\033[m\n"),
        ],
    )
    def test_color(self, capfd: CaptureFixture, stdout: StdText, expected: str) -> None:
        cprint(stdout)
        out, err = capfd.readouterr()
        assert out == expected
        assert err == ""

    @pytest.mark.parametrize(
        "stdout, expected",
        [
            (StdText("bg_black", Color.BG_BLACK), "\033[40mbg_black\033[m\n"),
            (StdText("bg_red", Color.BG_RED), "\033[41mbg_red\033[m\n"),
            (StdText("bg_green", Color.BG_GREEN), "\033[42mbg_green\033[m\n"),
            (StdText("bg_yellow", Color.BG_YELLOW), "\033[43mbg_yellow\033[m\n"),
            (StdText("bg_blue", Color.BG_BLUE), "\033[44mbg_blue\033[m\n"),
            (StdText("bg_magenta", Color.BG_MAGENTA), "\033[45mbg_magenta\033[m\n"),
            (StdText("bg_cyan", Color.BG_CYAN), "\033[46mbg_cyan\033[m\n"),
            (StdText("bg_white", Color.BG_WHITE), "\033[47mbg_white\033[m\n"),
        ],
    )
    def test_bg_color(
        self, capfd: CaptureFixture, stdout: StdText, expected: str
    ) -> None:
        cprint(stdout)
        out, err = capfd.readouterr()
        assert out == expected
        assert err == ""

    @pytest.mark.parametrize(
        "stdout, expected",
        [
            (StdText("bold", Format.BOLD), "\033[1mbold\033[m\n"),
            (StdText("faint", Format.FAINT), "\033[2mfaint\033[m\n"),
            (StdText("italic", Format.ITALIC), "\033[3mitalic\033[m\n"),
            (StdText("underline", Format.UNDERLINE), "\033[4munderline\033[m\n"),
            (StdText("blink", Format.BLINK), "\033[5mblink\033[m\n"),
            (StdText("fast_blink", Format.FAST_BLINK), "\033[6mfast_blink\033[m\n"),
            (StdText("reverse", Format.REVERSE), "\033[7mreverse\033[m\n"),
            (StdText("conceal", Format.CONCEAL), "\033[8mconceal\033[m\n"),
            (StdText("strike", Format.STRIKE), "\033[9mstrike\033[m\n"),
        ],
    )
    def test_format(
        self, capfd: CaptureFixture, stdout: StdText, expected: str
    ) -> None:
        cprint(stdout)
        out, err = capfd.readouterr()
        assert out == expected
        assert err == ""

    @pytest.mark.parametrize(
        "stdout, attrs, expected",
        [
            ("this is bold", [Format.BOLD], "\033[1mthis is bold\033[m\n"),
            ("this is faint", [Format.FAINT], "\033[2mthis is faint\033[m\n"),
            ("this is italic", [Format.ITALIC], "\033[3mthis is italic\033[m\n"),
            (
                "this is underline",
                [Format.UNDERLINE],
                "\033[4mthis is underline\033[m\n",
            ),
            ("this is blink", [Format.BLINK], "\033[5mthis is blink\033[m\n"),
            (
                "this is fast_blink",
                [Format.FAST_BLINK],
                "\033[6mthis is fast_blink\033[m\n",
            ),
            ("this is reverse", [Format.REVERSE], "\033[7mthis is reverse\033[m\n"),
            ("this is conceal", [Format.CONCEAL], "\033[8mthis is conceal\033[m\n"),
            ("this is strike", [Format.STRIKE], "\033[9mthis is strike\033[m\n"),
        ],
    )
    def test_attrs(
        self, capfd: CaptureFixture, stdout: StdText, attrs: list, expected: str
    ) -> None:
        cprint(stdout, attrs=attrs)
        out, err = capfd.readouterr()
        assert out == expected
        assert err == ""
