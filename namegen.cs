using System.IO;
using System;

class TechnoBabble
{
	private static string generateBritishName(Random rnd){

		string[] first = {"penny","padding","welling","evening","sun","tree","middle","swan","book","willow","grey","north","east","west","south","day","love","thorn","fitz","single","bert","fen","clark","con","bow","good","kay","hor","noble","eng","scot","wood","al","cliff","hod","whit","hale","gale"};
		string[] last = {"ton","smith","worth","hill","man","son","hunter","poole","lane","booth","well","cross","bird","lace","well","bank","witt","win","hope","ward","cock","en","wright","wick","house","head","on","way","den","bot","ley","field","croft"};
		string s = first[rnd.Next(0, first.Length)]+last[rnd.Next(0, last.Length)];
		s = s[0].ToString().ToUpper() + s.Substring(1);
		if(rnd.Next(100)<5){
			s = "Mc"+s;
		}
		return s;
	}

	private static string generateJapaneseishName(Random rnd){
		string s = "";
		string[] v = {"a","e","i","o","u"};
		string[] c = {"w","r","t","p","s","d","f","g","h","k","l","v","b","n","m"}; //Some letters are removed because they looked weird.
		int l = rnd.Next(4,9);
		for(int i=0; i<l; i++){
			if(i%2 == 0){
				int tmp = rnd.Next(0, c.Length);
				s += c[tmp];
			}
			else{
				s += v[rnd.Next(0, v.Length)];
			}
		}
		s = s[0].ToString().ToUpper() + s.Substring(1);
		return s;
	}

    static void generate(string gadgetType)
    {
        
    //string gadgetType = "Engine"; 
    
	//TODO: Kolla stavning!
	string[] buzzwords =  {"Quantum", "Dynamic", "Static", "Entangled", "Nano", "Relativistic", "Mega", "Super", "Celestial", "Ridgid", "Negative", "Frictionless", "Superconducting", "Particle", "Nuclear", "Evolutionary", "Ultra", "Hyper-G", "Low-Gravity", "Interstellar", "Viscous", "Inviscous", "Escalating","Timeless","Hyper", "Dangerous","Sparkly", "Boiling", "Bending", "Torsion", "Non-linear", "Linear", "Parabolic", "Hyperbolic", "Elliptical", "Conductive", "Cyclical", "Sustainable", "Caffeine-free", "Deep", "Improbabillity", "Infinite"};
	
	string[] names = {"Newton", "Gauss", "Euler", "Kepler", "Turing", "Lovelace", "Hawking","Beeblebrox", "Izzo", "Wittig", "Sapera", "Baier","Holgersson", "Selg", "Wase", "Brynte", "Turesson", "Nystrom"};
	string[] nouns = {"Lead", "Loop", "Portal", "Neutron", "Paper", "Plasma", "Solid","Gas","Liquid", "Fluid", "Galaxy", "Star", "Type-A", "Type-B", "Class 1", "Class 2", "Candy", "Sprinkle", "Hydra", "Stardust", "Light", "Combustion", "Electron", "Positron", "Boson", "Higgs-Boson", "Neutrino", "Tycheon", "Capacitor", "Flux", "Hexa", "Doca", "Octa", "Tetra", "Yarn", "Warp", "Torque", "Inertia", "Horizon", "Laser", "Core", "Master", "Pendulum", "Chaos", "Tequila", "Dream", "Honey"};
    
	Random rnd = new Random();
	int inventors = rnd.Next(1,2+1);
	string name = "";    

    if(rnd.Next(0,100)<40){
		for(int inv=0; inv<inventors; inv++){
			string s = "";
			int randtmp = rnd.Next(0,100);
			if(randtmp <10){
				s += names[rnd.Next(0, names.Length)];
			}
			else if(randtmp < 40){
				s = generateJapaneseishName( rnd );
			}
			else{
				s = generateBritishName( rnd );
			}
			name += s;
			if(inv!=inventors-1){
				name += "-";
			}
		}
		name = buzzwords[rnd.Next(0, buzzwords.Length)]+" "+name+" "+gadgetType;
	}
	else{
		name = buzzwords[rnd.Next(0, buzzwords.Length)]+" "+nouns[rnd.Next(0, nouns.Length)]+" "+gadgetType;
	}
	return name;
    
    }
}